import socket
from Class.ClientThread import ClientThread

class Server:
    def __init__(self) -> None:
        self.connections = []
        self.tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpsock.bind(("",1111))

    def run(self):
        while True:
            self.tcpsock.listen(10)
            print( "En écoute...")
            (clientsocket, (ip, port)) = self.tcpsock.accept()
            newthread = ClientThread(ip, port, clientsocket, self.connections)
            self.connections.append(newthread)
            newthread.start()

Server().run()