from databases.database_base import Database
import os

class Type(Database):

    def __init__(self,type_name):
        self.type_name = type_name
    
    @classmethod
    def get_all_types(cls):
        cls.cursor.execute("SELECT DISTINCT type FROM documents")
        info = cls.cursor.fetchall()
        types = [item[0] for item in info]
        return types
    
    def create_type(self):
        self.cursor.execute("INSERT INTO documents (type) VALUES (?)",(self.type_name,))
        self.conn.commit()
        os.mkdir('storage/'+self.type_name)
    
    def update_type(self,new_name):
        self.cursor.execute("UPDATE documents SET type = ? WHERE type = ?",(self.type_name,new_name,))
        self.conn.commit()

    def delete_type(self):
        self.cursor.execute("DELETE FROM documents WHERE type = ?",(self.type_name,))
        self.conn.commit()
        os.rmdir('storage/'+self.type_name)

    def exist(self):
        self.cursor.execute("SELECT type FROM documents WHERE type = ?",(self.type_name,))
        info = self.cursor.fetchone()
        return info != None