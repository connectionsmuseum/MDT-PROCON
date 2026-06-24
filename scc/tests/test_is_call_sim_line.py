import unittest

import evaluatecard as ec


class IsCallSimLineTests(unittest.TestCase):
    def _decoded_from_line_code(self, code):
        aa, bb, cc = code.split("-")
        return {
            "FT": int(aa[0]),
            "FU": int(aa[1]),
            "VG": int(bb),
            "HG": int(cc[0]),
            "VF": int(cc[1]),
        }

    def test_returns_true_for_known_call_sim_line(self):
        decoded = self._decoded_from_line_code(ec.CALL_SIM_LINES[0])
        self.assertTrue(ec.is_call_sim_line(decoded))

    def test_returns_true_for_all_configured_call_sim_lines(self):
        for line_code in ec.CALL_SIM_LINES:
            with self.subTest(line_code=line_code):
                decoded = self._decoded_from_line_code(line_code)
                self.assertTrue(ec.is_call_sim_line(decoded))

    def test_returns_false_for_non_member_line(self):
        decoded = {"FT": 9, "FU": 9, "VG": 99, "HG": 9, "VF": 9}
        self.assertFalse(ec.is_call_sim_line(decoded))


if __name__ == "__main__":
    unittest.main()
