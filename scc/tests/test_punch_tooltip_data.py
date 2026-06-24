import unittest

import public_sccweb as web


class PunchTooltipDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        web.app.testing = True
        cls.client = web.app.test_client()

    def test_punch_tooltip_data_returns_full_card_grid(self):
        response = self.client.get('/punch-tooltip-data')

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 18)
        self.assertTrue(all(len(row) == 69 for row in data))

        self.assertEqual(data[0][0]['name'], 'TI')
        self.assertIn('Trouble encountered', data[0][0]['description'])
        self.assertEqual(data[0][30]['name'], '-')
        self.assertIsNone(data[0][30]['description'])


if __name__ == '__main__':
    unittest.main()