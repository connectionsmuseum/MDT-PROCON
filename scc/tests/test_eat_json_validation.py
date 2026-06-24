import json
import os
import tempfile
import unittest

import card_storage
import public_sccweb as web


class EatJsonValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        web.app.testing = True
        cls.client = web.app.test_client()

    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self._prior_db_path = os.environ.get('CARD_DB_PATH')
        os.environ['CARD_DB_PATH'] = os.path.join(self._tmpdir.name, 'cards.db')

    def tearDown(self):
        if self._prior_db_path is None:
            os.environ.pop('CARD_DB_PATH', None)
        else:
            os.environ['CARD_DB_PATH'] = self._prior_db_path
        self._tmpdir.cleanup()

    def _valid_payload(self):
        return {
            'z_card': [
                [True, False, True],
                [False, True, False],
            ],
            'metadata': {
                'bin': 'UNIT_TEST_BIN',
                'register': {'digits': [1, 2, 3]},
            },
        }

    def test_accepts_valid_payload_and_persists_json(self):
        payload = self._valid_payload()
        response = self.client.post('/eat_json', json=payload)

        self.assertEqual(response.status_code, 200)

        stored_rows = card_storage.list_cards_with_payload()
        self.assertEqual(len(stored_rows), 1)
        _, saved_payload = stored_rows[0]
        self.assertEqual(saved_payload, payload)

    def test_rejects_non_json_content_type(self):
        response = self.client.post('/eat_json', data='{}', content_type='text/plain')
        self.assertEqual(response.status_code, 415)

    def test_rejects_unexpected_top_level_keys(self):
        payload = self._valid_payload()
        payload['surprise'] = 'nope'

        response = self.client.post('/eat_json', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()['error'], 'unexpected top-level keys')

    def test_rejects_non_object_json_body(self):
        response = self.client.post('/eat_json', json=[1, 2, 3])
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()['error'], 'request body must be a JSON object')

    def test_rejects_non_boolean_card_values(self):
        payload = self._valid_payload()
        payload['z_card'] = [[True, 1, False]]

        response = self.client.post('/eat_json', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()['error'], 'card values must be booleans')

    def test_rejects_ragged_card_rows(self):
        payload = self._valid_payload()
        payload['z_card'] = [[True, False], [True]]

        response = self.client.post('/eat_json', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()['error'], 'all card rows must have the same number of columns')

    def test_rejects_non_object_metadata(self):
        payload = self._valid_payload()
        payload['metadata'] = ['bad']

        response = self.client.post('/eat_json', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()['error'], 'metadata must be an object')

    def test_rejects_oversized_payload(self):
        oversize_blob = 'x' * (web.MAX_EAT_JSON_BYTES + 1)
        payload = {'z_card': [[True]], 'metadata': {'blob': oversize_blob}}
        raw = json.dumps(payload)

        response = self.client.post('/eat_json', data=raw, content_type='application/json')

        self.assertEqual(response.status_code, 413)


if __name__ == '__main__':
    unittest.main()