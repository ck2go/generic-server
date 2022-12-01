''' UDP Server.'''

import select
import socket
from time import sleep
from threading import Thread


def recv_timeout(sock, bytes_to_read, timeout_seconds):
    sock.setblocking(0)
    ready = select.select([sock], [], [], timeout_seconds)
    if ready[0]:
        return sock.recv(bytes_to_read)

    raise socket.timeout()

class UdpServer():
    def __init__(self, responder):
        self._responder = responder
        self.ip = "127.0.0.1"
        self.port = 20001
        self.buffer_size = 1024
        self.is_running = False
        self._run = False

    def run(self, timeout=1):
        self._run = True
        udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        res = udp_socket.bind((self.ip, self.port))
        print("UDP server up and listening")
        self.is_running = True

        while self._run:
            try:
                message_from_client, client_address = recv_timeout(udp_socket, self.buffer_size, timeout)
            except socket.timeout:
                continue

            print(f'Message from {client_address}: "{message_from_client}"')
            if message_from_client == 'MOCKSERVER:STOP':
                print('Waiting for server to stop...')
                self._run = False
            else:
                answer = 'ok'
                print(f'  Sending answer: "{answer}"')
                udp_socket.sendto(str.encode(answer), client_address)

        udp_socket.close()
        self.is_running = False
        print('Server stopped.')
