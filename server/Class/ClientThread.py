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