'''Module to run MockServer.'''

from __future__ import absolute_import
from .mockserver import MockServer

def main():
    my_server = MockServer()
    my_server.run()

    
