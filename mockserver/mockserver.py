'''The main MockServer class.'''

from __future__ import absolute_import
from .udpserver import UdpServer
from .tcpserver import TcpServer
from .mockresponder import MockResponderReflect

class MockServer():
    def __init__(self, protocol='udp', responder='reflect'):
        server = {'udp': UdpServer,
                  'tcp': TcpServer}[protocol]
        responders = {'reflect': MockResponderReflect}
        if responder in responders.keys():
            responder = responders[responder]()
        else:
            keys = str(list(responders.keys()))
            raise NotImplemented("Responder can't be any other type than string yet. Should be one of %s." % keys)
        self.server = server(responder=responder)

    def run(self):
        self.server.run()

    def stop(self):
        self.server.stop()

    @property
    def is_running(self):
        return self.server.is_running
