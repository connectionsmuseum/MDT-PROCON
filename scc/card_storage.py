import json
import os
import sqlite3
from datetime import datetime

_PREFERRED_DB_PATH = "/var/lib/scc/cards.db"
_FALLBACK_DB_PATH = "/tmp/cards/cards.db"
_resolved_auto_db_path = None


def get_db_path():
    """Resolve the SQLite file path from environment or default location."""
    return _resolve_db_path()


def _can_open_sqlite(db_path):
    try:
        db_dir = os.path.dirname(db_path)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)
        conn = sqlite3.connect(db_path)
        conn.close()
        return True
    except (OSError, sqlite3.Error):
        return False


def _resolve_db_path():
    global _resolved_auto_db_path

    configured = os.environ.get("CARD_DB_PATH")
    if configured:
        return configured

    if _resolved_auto_db_path is not None:
        return _resolved_auto_db_path

    for candidate in (_PREFERRED_DB_PATH, _FALLBACK_DB_PATH):
        if _can_open_sqlite(candidate):
            _resolved_auto_db_path = candidate
            return _resolved_auto_db_path

    raise RuntimeError("No writable SQLite storage path found for card database")


def is_using_fallback_path():
    """Return True when CARD_DB_PATH is unset and fallback path is active."""
    return os.environ.get("CARD_DB_PATH") is None and get_db_path() == _FALLBACK_DB_PATH


def _normalize_name_to_punchdate(name):
    base = os.path.basename(name)
    if base.lower().endswith(".json"):
        base = os.path.splitext(base)[0]
    if base.endswith("_front"):
        return base[:-6]
    return base


def _connect():
    db_path = get_db_path()
    db_dir = os.path.dirname(db_path)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS cards (
            punchdate TEXT PRIMARY KEY,
            created_at TEXT NOT NULL,
            payload_json TEXT NOT NULL,
            bin_name TEXT,
            register_digits_json TEXT
        )
        """
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_cards_created_at ON cards(created_at)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_cards_bin_name ON cards(bin_name)"
    )
    return conn


def initialize_storage():
    """Initialize schema and return the active database path."""
    with _connect() as conn:
        conn.execute("SELECT 1")
    return get_db_path()


def save_card_payload(punchdate, payload):
    metadata = payload.get("metadata", {}) if isinstance(payload, dict) else {}
    bin_name = metadata.get("bin") if isinstance(metadata, dict) else None
    register_digits = None
    if isinstance(metadata, dict):
        register = metadata.get("register", {})
        if isinstance(register, dict):
            register_digits = register.get("digits")

    register_digits_json = None
    if register_digits is not None:
        register_digits_json = json.dumps(register_digits, separators=(",", ":"))

    try:
        created_at = datetime.strptime(punchdate, "%y-%m-%d_%H-%M-%S-%f").isoformat(sep=" ")
    except ValueError:
        created_at = punchdate

    with _connect() as conn:
        conn.execute(
            """
            INSERT OR REPLACE INTO cards
                (punchdate, created_at, payload_json, bin_name, register_digits_json)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                punchdate,
                created_at,
                json.dumps(payload, separators=(",", ":")),
                bin_name,
                register_digits_json,
            ),
        )


def list_card_json_names(limit=None):
    query = "SELECT punchdate FROM cards ORDER BY punchdate DESC"
    params = ()
    if limit is not None:
        query += " LIMIT ?"
        params = (int(limit),)

    with _connect() as conn:
        rows = conn.execute(query, params).fetchall()
    return [f"{row['punchdate']}_front.json" for row in rows]


def load_card_payload(name):
    punchdate = _normalize_name_to_punchdate(name)
    with _connect() as conn:
        row = conn.execute(
            "SELECT payload_json FROM cards WHERE punchdate = ?",
            (punchdate,),
        ).fetchone()
    if row is None:
        return None
    return json.loads(row["payload_json"])


def list_cards_with_payload(limit=None):
    query = "SELECT punchdate, payload_json FROM cards ORDER BY punchdate DESC"
    params = ()
    if limit is not None:
        query += " LIMIT ?"
        params = (int(limit),)

    with _connect() as conn:
        rows = conn.execute(query, params).fetchall()

    out = []
    for row in rows:
        out.append((f"{row['punchdate']}_front.json", json.loads(row["payload_json"])))
    return out
