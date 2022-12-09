''' Responder reflecting a request.'''
from . import MockResponder

class Reflector(MockResponder):
    def respondTo(self, request):
        return request