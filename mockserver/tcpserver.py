''' TCP Server.'''

import socket


class TcpServer():
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 20001
        self.buffer_size = 1024
        self.running = False

    def run(self):
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind((self.ip, self.port))
        tcp_socket.listen()
        print("UDP server up and listening")
        self.running = True

        conn, client_address = tcp_socket.accept()
        with conn:
            print(f"Connected from {client_address}")
            while self.running:
                message_from_client = conn.recv(self.buffer_size)
                if not message_from_client:
                    break

                print(f'Message from {client_address}: "{message_from_client}"')

                answer = 'ok'
                print(f'  Sending answer: "{answer}"')
                conn.sendall(answer)

        tcp_socket.close()