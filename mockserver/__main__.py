"""Module to run MockServer."""

from .mockserver import MockServer


def main():
    """
    Starts the MockServer.
    """
    my_server = MockServer()
    my_server.run()

    
