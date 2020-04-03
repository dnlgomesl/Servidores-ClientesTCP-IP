import socket
import threading

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def sendMsg(self):
        while True:
            self.sock.send(input().encode('utf-8'))
    def __init__(self):
        self.sock.connect(('localhost', 9090))
        sendMThread = threading.Thread(target=self.sendMsg)
        sendMThread.daemon = True
        sendMThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
client = Client()