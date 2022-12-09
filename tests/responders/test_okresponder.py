from unittest import TestCase
from mockserver.responders.okresponder import OkResponder

class OkResponderTest(TestCase):
    def test_response(self):
        request = 'test'
        responder = OkResponder()
        response = responder.respondTo(request)
        self.assertEqual(response, 'ok', f"Response should always be 'ok'. Request: '{request}, Response: '{response}'")
