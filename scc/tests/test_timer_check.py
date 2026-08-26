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

    def test_call_type_getmeta_classifies_call_types(self):
        cases = (
            (("DR8",), "Dial Tone"),
            (("SOG",), "Subscriber Outgoing"),
            (("TER",), "Terminating"),
            (("ITR", "FLG"), "Intraoffice Forward Linkage"),
            (("ITR", "SCB"), "Intraoffice Callback Linkage"),
            (("TOG",), "Tandem Outgoing"),
        )
        for punches, expected in cases:
            with self.subTest(punches=punches):
                card = self._blank_card()
                self._punch(card, *punches)
                self.assertEqual(ec.call_type_getmeta(card), expected)

    def test_call_type_getmeta_returns_none_for_unknown_call(self):
        self.assertIsNone(ec.call_type_getmeta(self._blank_card()))

    def test_none_when_no_timer(self):
        card = self._blank_card()
        self.assertIsNone(ec.timer_check(card))

    def test_non_sdt_timer_returns_structured_metadata(self):
        card = self._blank_card()
        self._punch(card, "TGT")

        result = ec.timer_check(card)

        self.assertEqual(result["timer"], "TGT")
        self.assertEqual(result["detected"], ["TGT"])
        self.assertIn("tgt", result)
        self.assertNotIn("sdt", result)

    def test_detected_list_includes_multiple_timers(self):
        card = self._blank_card()
        self._punch(card, "TGT", "SDT")

        result = ec.timer_check(card)

        self.assertEqual(result["timer"], "SDT")
        self.assertEqual(result["detected"], ["SDT", "TGT"])
        self.assertIn("sdt", result)
        self.assertNotIn("tgt", result)

    def test_wt_missing_first_recycle_includes_metadata(self):
        card = self._blank_card()
        self._punch(card, "WT", "DR8")

        with self.assertRaises(ec.TimerCheckError) as exc_info:
            ec.timer_check(card)

        self.assertEqual(exc_info.exception.code, "WT_FAILURE")
        self.assertEqual(exc_info.exception.bin, "WT_FAILURE")
        self.assertEqual(exc_info.exception.details["required"], ["TK", "GLH"])
        self.assertEqual(exc_info.exception.details["missing"], ["TK", "GLH"])
        self.assertEqual(exc_info.exception.details["first_missing_recycle"], "TK")
        self.assertNotIn("expected_recycles", exc_info.exception.details)
        self.assertNotIn("missing_recycles", exc_info.exception.details)
        self.assertNotIn("triggered_by", exc_info.exception.details)

    def test_wt_missing_second_recycle_includes_metadata(self):
        card = self._blank_card()
        self._punch(card, "WT", "SOG", "TK")

        with self.assertRaises(ec.TimerCheckError) as exc_info:
            ec.timer_check(card)

        self.assertEqual(exc_info.exception.details["required"], ["TK", "GLH"])
        self.assertEqual(exc_info.exception.details["missing"], ["GLH"])
        self.assertEqual(exc_info.exception.details["first_missing_recycle"], "GLH")

    def test_wt_with_all_expected_recycles_returns_metadata(self):
        card = self._blank_card()
        self._punch(card, "WT", "TOG", "HTUK", "GLH")

        result = ec.timer_check(card)

        self.assertTrue(result["wt"]["implemented"])
        self.assertEqual(result["wt"]["required"], ["HTUK", "GLH"])
        self.assertEqual(result["wt"]["missing"], [])

    def test_wt_rng_credits_htuk_recycle(self):
        card = self._blank_card()
        self._punch(card, "WT", "TER", "RNG", "GLH")

        result = ec.timer_check(card)

        self.assertEqual(result["wt"]["required"], ["HTUK", "GLH"])
        self.assertEqual(result["wt"]["missing"], [])

    def test_wt_rng_still_requires_glh(self):
        card = self._blank_card()
        self._punch(card, "WT", "TER", "RNG")

        with self.assertRaises(ec.TimerCheckError) as exc_info:
            ec.timer_check(card)

        self.assertEqual(exc_info.exception.details["missing"], ["GLH"])
        self.assertIn("HTUK", exc_info.exception.details["found"])
        self.assertEqual(exc_info.exception.details["first_missing_recycle"], "GLH")

    def test_wt_unknown_call_is_failure(self):
        card = self._blank_card()
        self._punch(card, "WT")

        with self.assertRaises(ec.TimerCheckError) as exc_info:
            ec.timer_check(card)

        self.assertEqual(exc_info.exception.code, "WT_FAILURE")
        self.assertNotIn("call_type", exc_info.exception.details)

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

    def test_sdt_ter_mak1_sng_rng_satisfies_ngk(self):
        card = self._blank_card()
        self._punch(card, "SDT", "TER", "CK", "MAK1", "SNG", "RNG", "LFK")

        result = ec.timer_check(card)

        rule = result["sdt"]["matched_rules"][1]
        self.assertEqual(rule["required"], ["NGK"])
        self.assertEqual(rule["present"], ["NGK"])
        self.assertTrue(rule["ok"])

    def test_sdt_itr_flg_mak1_rng_satisfies_ngk(self):
        card = self._blank_card()
        self._punch(card, "SDT", "ITR", "FLG", "MAK1", "RNG", "SNG")

        result = ec.timer_check(card)

        rule = result["sdt"]["matched_rules"][0]
        self.assertEqual(rule["required"], ["NGK"])
        self.assertEqual(rule["present"], ["NGK"])
        self.assertTrue(rule["ok"])

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
