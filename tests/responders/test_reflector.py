from unittest import TestCase
from mockserver.responders.reflector import Reflector

class ReflectorTest(TestCase):
    def test_reflect(self):
        request = 'test'
        reflector = Reflector()
        response = reflector.respondTo(request)
        self.assertEqual(request, response, f'The reflector should just return the request. Request: {request}, Response: {response}')
