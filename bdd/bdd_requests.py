import sqlite3

class BDD:
    def __init__(self, path) -> None:
        self.connection = sqlite3.connect(path)
    
    def open_cursor(self):
        return self.connection.cursor()
    
    def close_cursor(self, cursor):
        cursor.close()
    
    def close_bdd(self):
        self.connection.close()

    def register(self, username, password):
        cursor = self.open_cursor()
        request = f"INSERT INTO Account VALUES (?,?);"
        cursor.execute(request, (username, password))
        self.connection.commit()
        self.close_cursor(cursor) 
    
    def create_Groupe(self, name):
        cursor = self.open_cursor()
        request = f"INSERT INTO Group VALUES (?);"
        cursor.execute(request, (name))
        self.connection.commit()
        self.close_cursor(cursor)

    def create_RelateGroupe(self, username, id_group):
        cursor = self.open_cursor()
        request = f"INSERT INTO RelateGroup VALUES (?,?);"
        cursor.execute(request, (username, id_group))
        self.connection.commit()
        self.close_cursor(cursor)

    def create_RelateAccount(self, username1, username2):
        cursor = self.open_cursor()
        request = f"INSERT INTO RelateAccount VALUES (?,?);"
        cursor.execute(request, (username1, username2))
        self.connection.commit()
        self.close_cursor(cursor)
    
    def get_Account(self, username):
        cursor = self.open_cursor()
        request = f"SELECT * FROM Account WHERE username = ?;"
        cursor.execute(request, (username,))
        value = cursor.fetchone()
        self.close_cursor(cursor)
        dicto = {"username": value[0], "password": value[1]}
        return dicto
    
    def get_party(self, pseudo):
        cursor = self.open_cursor()
        request = f"SELECT * FROM Party WHERE player = ?;"
        cursor.execute(request, (pseudo,))
        value = cursor.fetchone()
        self.close_cursor(cursor)
        dicto = {"pseudo": value[0], "timer": value[1], "level": value[2], "map": value[3]}
        return dicto
        
    def get_all(self):
        cursor = self.open_cursor()
        request = f"SELECT * FROM Party JOIN Player ON Player.pseudo = Party.player ORDER BY level DESC, timer ASC"
        cursor.execute(request)
        values = cursor.fetchall()
        self.close_cursor(cursor)
        dicto_all = []
        for value in values:
            dicto_all.append({"rank": values.index(value)+1,"pseudo": value[0], "timer": value[1], "level": value[2], "map": value[3], "character": value[5]})
        return dicto_all
    
    def update_party(self, pseudo, timer=None, level=None, map=None):
        if timer==None or level==None or map==None:
            result = self.get_party(pseudo)
            if timer == None:
                timer = result["timer"]
            if level == None:
                level = result["level"]
            if map == None:
                map = result["map"]
        cursor = self.open_cursor()
        request = f"UPDATE Party SET timer = ?, level = ?, map = ? WHERE player = ?"
        cursor.execute(request, (timer, level, map, pseudo))
        self.connection.commit()