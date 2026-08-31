import os
import tempfile
import unittest

import card_storage
import delete_card


class DeleteCardTests(unittest.TestCase):
    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self._prior_db_path = os.environ.get("CARD_DB_PATH")
        os.environ["CARD_DB_PATH"] = os.path.join(self._tmpdir.name, "cards.db")
        self.punchdate = "26-08-28_12-34-56-123456"
        card_storage.save_card_payload(self.punchdate, {"z_card": [[True]]})

    def tearDown(self):
        if self._prior_db_path is None:
            os.environ.pop("CARD_DB_PATH", None)
        else:
            os.environ["CARD_DB_PATH"] = self._prior_db_path
        self._tmpdir.cleanup()

    def test_deletes_card_for_supported_url_forms(self):
        forms = (
            self.punchdate,
            f"{self.punchdate}_front",
            f"{self.punchdate}_front.json",
            f"https://cards.example/card/{self.punchdate}_front",
        )

        for card_url in forms:
            with self.subTest(card_url=card_url):
                card_storage.save_card_payload(self.punchdate, {"z_card": [[True]]})
                self.assertTrue(delete_card.delete_card(card_url))
                self.assertIsNone(card_storage.load_card_payload(self.punchdate))

    def test_reports_missing_card_without_deleting_other_cards(self):
        self.assertFalse(delete_card.delete_card("/card/26-08-28_00-00-00_front"))
        self.assertIsNotNone(card_storage.load_card_payload(self.punchdate))

    def test_rejects_url_without_a_card_identifier(self):
        with self.assertRaises(ValueError):
            delete_card.card_name_from_url("https://cards.example/")


if __name__ == "__main__":
    unittest.main()