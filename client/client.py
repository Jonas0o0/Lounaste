# coding: utf-8

import socket



class ClassClient:
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.s.connect((self.ip, self.port))
        a = True
        while a:
            file_name = input("envoyer un message (quit pour quitter) >> ") # utilisez raw_input() pour les anciennes versions python
            self.s.send(file_name.encode())
            if file_name == "quit":
                a = False
            if file_name[:9].lower() == 'send all:':
                response = self.s.recv(255).decode()
                if response != "":
                    print(response)
        self.s.close()
        print('Déconnexion from {}'.format(self.port))
        
    def send(self, data):
        self.s.connect((self.ip, self.port))
        self.s.send(data.encode())
        response = self.s.recv(255).decode()
        if response != "":
            self.s.close()
            print('Déconnexion from {}'.format(self.port))
            return response
        



a = ClassClient("172.16.39.18", 1111)
a.run()