from unittest import TestCase
from unittest.mock import patch
from mockserver.responders.manual import ManualResponder


class ManualResponderTest(TestCase):
    @patch('builtins.input')
    def test_reflect(self, mock_input):
        manual_response = '42'
        mock_input.return_value = manual_response

        request = 'test'
        reflector = ManualResponder()
        response = reflector.respondTo(request)
        self.assertEqual(manual_response, response, f"The manual responder should return the answer entered by the user. Request: '{request}', Response: '{response}'")
