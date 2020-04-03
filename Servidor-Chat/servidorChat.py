import socket
import threading

class Servidor:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('localhost', 9090))
        self.sock.listen(1)
        print("Servidor no ar...")

    def sendMsg(self, conn, msg):
        print(msg)
        for connection in self.connections:
            if(connection != conn):
                connection.send(msg.encode('utf-8'))


    def customer(self, conn, addr):
        while True:
            msg = ''
            data = conn.recv(1024)
            if data.decode('utf-8').upper() == 'BYE':
                msg = '> ' + str(addr[0]) + ':' + str(addr[1]) + ' - disconnected'
                self.sendMsg(conn, msg)
                self.connections.remove(conn)
                conn.close()
                break
            else:
                msg = '> ' + str(addr[0]) + ':' + str(addr[1]) + ' - ' + data.decode('utf-8')
            self.sendMsg(conn, msg)

    def run(self):
        while True:
            conn, addr = self.sock.accept()
            cThread = threading.Thread(target=self.customer, args=(conn,addr))
            cThread.daemon = True
            cThread.start()
            self.connections.append(conn)
            print(str(addr[0]) + ':' + str(addr[1]) + ' - connected')

server = Servidor()
server.run()