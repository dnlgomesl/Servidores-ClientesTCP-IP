import socket
import threading

class Servidor:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self):
        self.sock.bind(('localhost', 9090))
        self.sock.listen(1)
        print("Servidor no ar...")

    def customer(self, conn, addr):
        while True:
            data = conn.recv(1024)
            if data.decode('utf-8').upper() == 'FIM':
                msg = str(addr[0]) + ':' + str(addr[1]) + ' - disconnected'
                print(msg)
                conn.close()
                break
            msg = '> ' + data.decode('utf-8')
            print(str(addr[0]) + ":" + str(addr[1]) + ' - ' + data.decode('utf-8'))
            conn.send(msg.encode('utf-8'))


    def run(self):
        while True:
            conn, addr = self.sock.accept()
            cThread = threading.Thread(target=self.customer, args=(conn,addr))
            cThread.daemon = True
            cThread.start()
            print(str(addr[0]) + ':' + str(addr[1]) + ' - connected')

server = Servidor()
server.run()