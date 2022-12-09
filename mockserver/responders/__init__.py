'''Respnders for the MockServer.'''

from abc import ABC
from abc import abstractmethod


class MockResponder(ABC):
    def __int__(self):
        pass

    @abstractmethod
    def respondTo(self, request):
        pass