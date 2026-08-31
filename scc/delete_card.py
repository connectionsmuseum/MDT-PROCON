#!/usr/bin/python3
import argparse
import os
from urllib.parse import unquote, urlparse

import card_storage


def card_name_from_url(card_url):
    """Return the card identifier from a card URL, path, or filename."""
    parsed = urlparse(card_url)
    path = parsed.path.rstrip("/")
    name = os.path.basename(unquote(path))
    if not name:
        raise ValueError("card URL must include a card identifier")
    return name


def delete_card(card_url):
    """Delete the card referenced by a URL, returning whether it existed."""
    return card_storage.delete_card_payload(card_name_from_url(card_url))


def main():
    parser = argparse.ArgumentParser(
        description="Delete one saved card by its card URL or filename."
    )
    parser.add_argument(
        "card_url",
        help="Card URL, path, filename, or ID (with or without _front)",
    )
    parser.add_argument(
        "--db-path",
        default=None,
        help="Database path. Defaults to CARD_DB_PATH or the application default.",
    )
    args = parser.parse_args()

    if args.db_path:
        os.environ["CARD_DB_PATH"] = args.db_path

    db_path = card_storage.initialize_storage()
    try:
        deleted = delete_card(args.card_url)
    except ValueError as exc:
        parser.error(str(exc))

    if not deleted:
        parser.error("card was not found")

    print(f"Deleted card from {db_path}")


if __name__ == "__main__":
    main()