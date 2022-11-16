'''Module to run MockServer.'''

from __future__ import absolute_import
from .udpserver import UdpServer
from .tcpserver import TcpServer


class MockServer():
    def __init__(self, protocol='udp'):
        self.server = {'udp': UdpServer(),
                       'tcp': TcpServer()}[protocol]

    def run(self):
        self.server.run()

    def stop(self):
        self.server.stop()

    @property
    def is_running(self):
        return self.server.is_running


def main():
    my_server = MockServer()
    my_server.run()

    
