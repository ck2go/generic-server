"""Responder waiting for a manual entry as a response."""

from . import MockResponder


class ManualResponder(MockResponder):
    def respondTo(self, request):
        return input(f"Please enter response to request '{request}': ")
