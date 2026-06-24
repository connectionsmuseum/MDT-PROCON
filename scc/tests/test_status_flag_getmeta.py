import unittest

import cardmap as cm
import evaluatecard as ec


class StatusFlagGetMetaTests(unittest.TestCase):
    def _blank_card(self):
        return [[False for _ in range(69)] for _ in range(18)]

    def _punch(self, card, *names):
        for name in names:
            row, col = cm.punchCoords(name)
            card[row][col] = True

    def test_prints_and_verifies_status_flag_getmeta(self):
        empty_card = self._blank_card()
        empty_result = ec.status_flag_getmeta(empty_card)
        print(f"status_flag_getmeta(empty) -> {empty_result}")
        self.assertIsNone(empty_result)

        single_true_card = self._blank_card()
        self._punch(single_true_card, "FCG")
        single_result = ec.status_flag_getmeta(single_true_card)
        print(f"status_flag_getmeta(single FCG) -> {single_result}")
        self.assertEqual(single_result, "FCG")

        multiple_true_card = self._blank_card()
        self._punch(multiple_true_card, "TRS", "DCK")
        multiple_result = ec.status_flag_getmeta(multiple_true_card)
        print(f"status_flag_getmeta(multiple TRS,DCK) -> {multiple_result}")
        self.assertEqual(multiple_result, ["TRS", "DCK"])


if __name__ == "__main__":
    unittest.main()
