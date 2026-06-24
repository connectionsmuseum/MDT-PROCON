import unittest

import sccweb as web


class _DummyResponse:
    def __init__(self, status_code):
        self.status_code = status_code


class SccWebForwardingTests(unittest.TestCase):
    def setUp(self):
        self._orig_url = web.PUBLIC_EAT_CARD_URL
        self._orig_timeout = web.PUBLIC_EAT_CARD_TIMEOUT_SECONDS
        self._orig_post = web.requests.post

    def tearDown(self):
        web.PUBLIC_EAT_CARD_URL = self._orig_url
        web.PUBLIC_EAT_CARD_TIMEOUT_SECONDS = self._orig_timeout
        web.requests.post = self._orig_post

    def test_forward_skips_when_url_not_configured(self):
        called = {"value": False}

        def fake_post(*args, **kwargs):
            called["value"] = True
            return _DummyResponse(200)

        web.PUBLIC_EAT_CARD_URL = ""
        web.requests.post = fake_post

        web._forward_card_to_public({"z_card": [[True]], "metadata": {}})

        self.assertFalse(called["value"])

    def test_forward_posts_payload_when_url_configured(self):
        seen = {}

        def fake_post(url, json, timeout):
            seen["url"] = url
            seen["json"] = json
            seen["timeout"] = timeout
            return _DummyResponse(200)

        payload = {"z_card": [[True, False]], "metadata": {"bin": "FWD"}}
        web.PUBLIC_EAT_CARD_URL = "https://example.org/eat_json"
        web.PUBLIC_EAT_CARD_TIMEOUT_SECONDS = 4.5
        web.requests.post = fake_post

        web._forward_card_to_public(payload)

        self.assertEqual(seen["url"], "https://example.org/eat_json")
        self.assertEqual(seen["json"], payload)
        self.assertEqual(seen["timeout"], 4.5)


if __name__ == "__main__":
    unittest.main()
