'''Classes for resonding to request strings.'''
from abc import ABC
from abc import abstractmethod


class MockResponder(ABC):
    def __int__(self):
        pass

    @abstractmethod
    def respondToRequest(self, request):
        pass


class MockResponderReflect(MockResponder):
    def respondToRequest(self, request):
        return request
