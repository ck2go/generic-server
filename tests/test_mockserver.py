from __future__ import absolute_import

from unittest import TestCase
from mockserver.__main__ import MockServer


class TestMockServer(TestCase):
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def setup_method(self, test_method):
        pass

    def teardown_method(self, test_method):
        pass

    def test_init(self):
        my_server = MockServer()
        assert isinstance(my_server, MockServer)

    def test_run(self):
        my_server = MockServer()
        res = my_server.run()
        assert res is None
