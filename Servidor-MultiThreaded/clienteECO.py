import socket

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self):
        self.sock.connect(('localhost', 9090))
        while True:
            self.sock.send(input().encode('utf-8'))
            data = self.sock.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
client = Client()