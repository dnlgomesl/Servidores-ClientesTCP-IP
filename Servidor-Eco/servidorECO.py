import socket

class Servidor:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientes = 0
    def __init__(self):
        self.sock.bind(('localhost', 9090))
        self.sock.listen(1)
        print("Servidor no ar...")

    def run(self):
        conn, addr = self.sock.accept()
        print(str(addr[0]) + ':' + str(addr[1]) + ' - connected')
        self.clientes += 1
        while True:
            if(self.clientes > 0):
                data = conn.recv(1024)
                if data.decode('utf-8').upper() == 'FIM':
                    print(str(addr[0]) + ':' + str(addr[1]) + ' - disconnected')
                    conn.close()
                    self.clientes -=1
                else:
                    print(str(addr[0]) + ':' + str(addr[1]) + ' - ' + data.decode('utf-8'))
                    conn.send(('> ' + data.decode('utf-8')).encode('utf-8'))
            else:
                conn, addr = self.sock.accept()
                print(str(addr[0]) + ':' + str(addr[1]) + ' - connected')
                self.clientes += 1     

server = Servidor()
server.run()
