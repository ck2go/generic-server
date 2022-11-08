''' UDP Server.'''

import socket


class UdpServer():
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 20001
        self.buffer_size = 1024
        self.running = False

    def run(self):
        udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        udp_socket.bind((self.ip, self.port))
        self.running = True
        print("UDP server up and listening")

        while self.running:
            message_from_client, client_address = udp_socket.recvfrom(self.buffer_size)

            print(f'Message from {client_address}: "{message_from_client}"')
            answer = 'ok'
            print(f'  Sending answer: "{answer}"')
            udp_socket.sendto(str.encode(answer), client_address)