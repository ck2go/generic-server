'''Responder always answering with 'ok'.'''

from . import MockResponder

class OkResponder(MockResponder):
    def respondTo(self, request):
        return 'ok'