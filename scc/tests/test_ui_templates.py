import os
import tempfile
import unittest

import card_storage
import public_sccweb as web


class UiTemplateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        web.app.testing = True
        cls.client = web.app.test_client()

    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self._prior_db_path = os.environ.get('CARD_DB_PATH')
        os.environ['CARD_DB_PATH'] = os.path.join(self._tmpdir.name, 'cards.db')
        self._original_get_offsets = web.get_offsets
        web.get_offsets = lambda: (0, 0, 0, 0, 0, 0)

    def tearDown(self):
        if self._prior_db_path is None:
            os.environ.pop('CARD_DB_PATH', None)
        else:
            os.environ['CARD_DB_PATH'] = self._prior_db_path
        self._tmpdir.cleanup()
        web.get_offsets = self._original_get_offsets

    def test_settings_page_has_home_metadata_toggle(self):
        response = self.client.get('/settings')

        self.assertEqual(response.status_code, 200)
        page = response.get_data(as_text=True)
        self.assertIn('id="displayCardMetadataHome"', page)
        self.assertIn('Display card metadata on home page', page)

    def test_home_page_includes_shared_metadata_panel(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        page = response.get_data(as_text=True)
        self.assertIn('/static/card_metadata.js', page)
        self.assertIn('/static/card_metadata.css', page)
        self.assertIn('id="home-metadata-panel"', page)

    def test_card_urls_are_extensionless_and_legacy_json_urls_still_work(self):
        payload = {
            'z_card': [[True, False], [False, True]],
            'metadata': {'bin': 'URL_TEST_BIN'}
        }
        post_response = self.client.post('/eat_json', json=payload)
        self.assertEqual(post_response.status_code, 200)

        names = card_storage.list_card_json_names(limit=1)
        self.assertEqual(len(names), 1)
        base_name = os.path.splitext(names[0])[0]

        bins_response = self.client.get('/bins')
        self.assertEqual(bins_response.status_code, 200)
        bins_page = bins_response.get_data(as_text=True)
        self.assertIn(f'/card/{base_name}', bins_page)
        self.assertNotIn(f'/card/{base_name}.json', bins_page)

        new_url_response = self.client.get(f'/card/{base_name}')
        legacy_url_response = self.client.get(f'/card/{base_name}.json')
        self.assertEqual(new_url_response.status_code, 200)
        self.assertEqual(legacy_url_response.status_code, 200)


if __name__ == '__main__':
    unittest.main()