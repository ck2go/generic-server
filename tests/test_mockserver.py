from __future__ import absolute_import

from unittest import TestCase
from mockserver.__main__ import MockServer
from mockserver.udpserver import UdpServer
from mockserver.tcpserver import TcpServer


class TestMockServer(TestCase):
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def setup_method(self, test_method):
        pass

    def teardown_method(self, test_method):
        pass

    def test_init_udpServer(self):
        my_server = MockServer(protocol='udp')
        assert isinstance(my_server, MockServer)
        assert isinstance(my_server.server, UdpServer)

    def test_init_tcpServer(self):
        my_server = MockServer(protocol='tcp')
        assert isinstance(my_server, MockServer)
        assert isinstance(my_server.server, TcpServer)

    def test_run(self):
        my_server = MockServer()
        res = my_server.run()
        assert res is None
