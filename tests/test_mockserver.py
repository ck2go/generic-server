from __future__ import absolute_import

# from unittest import TestCase
from unittest.mock import Mock

from mockserver.__main__ import MockServer
from mockserver.tcpserver import TcpServer
from mockserver.udpserver import UdpServer


class TestMockServer:
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

    def test_udp_run_got_stop(self, mocker):
        # set up mocks
        mock_sock = mocker.patch('mockserver.udpserver.socket.socket')
        mock_sock.return_value.bind.return_value = 'bound'
        mock_sock.return_value.setblocking.return_value = None
        mock_sock.return_value.recv.return_value = ('MOCKSERVER:STOP', ('127.0.0.1', 20001))

        mocker.patch("mockserver.udpserver.select.select", return_value=[True, True])

        # run mock server
        my_server = MockServer()
        my_server.run()

        mock_sock.assert_called_once()
        mock_sock.return_value.recv.assert_called_once()

    def test_tcp_run_got_stop(self, mocker):
        # set up mocks
        mock_conn = Mock()
        mock_conn.__enter__ = lambda *args: True
        mock_conn.__exit__ = lambda *args: True
        mock_conn.recv.return_value = 'MOCKSERVER:STOP'

        mock_sock = mocker.patch('mockserver.udpserver.socket.socket')
        mock_sock.return_value.bind.return_value = None
        mock_sock.return_value.listen.return_value = None
        mock_sock.return_value.setblocking.return_value = None
        mock_sock.return_value.accept.return_value = (mock_conn, ('127.0.0.1', 20001))

        mocker.patch("mockserver.udpserver.select.select", return_value=[True, True])

        # run mock server
        my_server = MockServer(protocol='tcp')
        my_server.run()

        mock_sock.assert_called_once()
        mock_conn.recv.assert_called_once()




