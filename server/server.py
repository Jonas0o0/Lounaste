import socket
import threading



class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket, connections):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        self.connections = connections
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
   
        print("Connexion de %s %s" % (self.ip, self.port, ))
        running = True
        while running:
            response = self.clientsocket.recv(255).decode()
            if response != '':
                print(response)
            if response[:9].lower() == "send all:":
                for client in self.connections:
                    client.clientsocket.send(response[10:].encode())
            if response == 'quit':
                running = False


        print("Client déconnecté...")

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