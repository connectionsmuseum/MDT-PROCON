import unittest

import cardmap as cm
import evaluatecard as ec


class TimerCheckTests(unittest.TestCase):
    def _blank_card(self):
        return [[False for _ in range(69)] for _ in range(18)]

    def _punch(self, card, *names):
        for name in names:
            row, col = cm.punchCoords(name)
            card[row][col] = True

    def test_none_when_no_timer(self):
        card = self._blank_card()
        self.assertIsNone(ec.timer_check(card))

    def test_non_sdt_timer_returns_structured_metadata(self):
        card = self._blank_card()
        self._punch(card, "WT")

        result = ec.timer_check(card)

        self.assertEqual(result["timer"], "WT")
        self.assertEqual(result["detected"], ["WT"])
        self.assertIn("wt", result)
        self.assertNotIn("sdt", result)

    def test_detected_list_includes_multiple_timers(self):
        card = self._blank_card()
        self._punch(card, "WT", "SDT")

        result = ec.timer_check(card)

        self.assertEqual(result["timer"], "WT")
        self.assertEqual(result["detected"], ["WT", "SDT"])
        self.assertIn("wt", result)
        self.assertNotIn("sdt", result)

    def test_tgt_timer_is_detected_and_dynamic(self):
        card = self._blank_card()
        self._punch(card, "TGT")

        result = ec.timer_check(card)

        self.assertEqual(result["timer"], "TGT")
        self.assertEqual(result["detected"], ["TGT"])
        self.assertIn("tgt", result)
        self.assertNotIn("sdt", result)

    def test_sdt_dial_tone_missing_ck(self):
        card = self._blank_card()
        self._punch(card, "SDT", "DR8", "FTCK")

        with self.assertRaises(ec.TimerCheckError) as exc_info:
            ec.timer_check(card)

        self.assertEqual(exc_info.exception.code, "DR8_FTCK_REQUIRES_CK")
        self.assertEqual(exc_info.exception.bin, "SDT_FAILURE")
        self.assertIn("CK", exc_info.exception.details["missing"])

    def test_sdt_sog_missing_osk(self):
        card = self._blank_card()
        self._punch(card, "SDT", "SOG", "OSG1")

        with self.assertRaises(ec.TimerCheckError) as exc_info:
            ec.timer_check(card)

        self.assertEqual(exc_info.exception.code, "SOG_OSG_REQUIRES_OSK")

    def test_sdt_ter_mak1_sng_missing_ngk(self):
        card = self._blank_card()
        self._punch(card, "SDT", "TER", "CK", "MAK1", "SNG")

        with self.assertRaises(ec.TimerCheckError) as exc_info:
            ec.timer_check(card)

        self.assertEqual(exc_info.exception.code, "TER_MAK1_SNG_REQUIRES_NGK")

    def test_sdt_itr_flg_ftck_missing_fs(self):
        card = self._blank_card()
        self._punch(card, "SDT", "ITR", "FLG", "FTCK")

        with self.assertRaises(ec.TimerCheckError) as exc_info:
            ec.timer_check(card)

        self.assertEqual(exc_info.exception.code, "ITR_FLG_FTCK_REQUIRES_FS")

    def test_sdt_tog_mak1_missing_ngk(self):
        card = self._blank_card()
        self._punch(card, "SDT", "TOG", "MAK1")

        with self.assertRaises(ec.TimerCheckError) as exc_info:
            ec.timer_check(card)

        self.assertEqual(exc_info.exception.code, "TOG_MAK1_REQUIRES_NGK")

    def test_sdt_sog_tgt_sets_timeout_cause(self):
        card = self._blank_card()
        self._punch(card, "SDT", "SOG", "TGT")

        with self.assertRaises(ec.TimerCheckError) as exc_info:
            ec.timer_check(card)

        self.assertEqual(exc_info.exception.code, "SOG_TGT_TIMEOUT")


if __name__ == "__main__":
    unittest.main()
