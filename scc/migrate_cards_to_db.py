#!/usr/bin/python3
import argparse
import glob
import json
import os

import card_storage


def _punchdate_from_filename(path):
    name = os.path.basename(path)
    suffix = "_front.json"
    if not name.endswith(suffix):
        return None
    return name[: -len(suffix)]


def migrate(source_dir, dry_run=False):
    pattern = os.path.join(source_dir, "*_front.json")
    files = sorted(glob.glob(pattern))

    imported = 0
    skipped = 0
    failed = 0

    for path in files:
        punchdate = _punchdate_from_filename(path)
        if not punchdate:
            skipped += 1
            continue

        try:
            with open(path) as handle:
                payload = json.load(handle)
            if not isinstance(payload, dict):
                raise ValueError("payload is not a JSON object")
            if not dry_run:
                card_storage.save_card_payload(punchdate, payload)
            imported += 1
        except Exception as exc:
            failed += 1
            print(f"ERROR {path}: {exc}")

    return {
        "files_found": len(files),
        "imported": imported,
        "failed": failed,
        "skipped": skipped,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Import legacy /tmp/cards/*_front.json files into SQLite storage."
    )
    parser.add_argument(
        "--source-dir",
        default="/tmp/cards",
        help="Directory containing legacy *_front.json files (default: /tmp/cards)",
    )
    parser.add_argument(
        "--db-path",
        default=None,
        help="Target SQLite DB path. Defaults to CARD_DB_PATH or app default.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse and validate files without writing to the DB.",
    )
    args = parser.parse_args()

    if args.db_path:
        os.environ["CARD_DB_PATH"] = args.db_path

    db_path = card_storage.initialize_storage()
    summary = migrate(args.source_dir, dry_run=args.dry_run)

    mode = "DRY RUN" if args.dry_run else "MIGRATION"
    print(f"{mode} complete")
    print(f"DB path: {db_path}")
    print(f"Source: {args.source_dir}")
    print(f"Files found: {summary['files_found']}")
    print(f"Imported: {summary['imported']}")
    print(f"Failed: {summary['failed']}")
    print(f"Skipped: {summary['skipped']}")


if __name__ == "__main__":
    main()
