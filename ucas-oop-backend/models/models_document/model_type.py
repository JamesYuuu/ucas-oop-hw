from databases.database_base import Database
import os

class Type(Database):

    def __init__(self,type):
        self.type = type
    
    @classmethod
    def get_all_types(cls):
        cls.cursor.execute("SELECT DISTINCT type FROM documents")
        info = cls.cursor.fetchall()
        types = [item[0] for item in info]
        return types
    
    def create_type(self):
        self.cursor.execute("INSERT INTO documents (type) VALUES (?)",(self.type,))
        self.conn.commit()
        os.mkdir('storage/'+self.type)
    
    def update_type(self,new_name):
        self.cursor.execute("UPDATE documents SET type = ? WHERE type = ?",(self.type,new_name,))
        self.conn.commit()

    def delete_type(self):
        self.cursor.execute("DELETE FROM documents WHERE type = ?",(self.type,))
        self.conn.commit()
        os.rmdir('storage/'+self.type)

    def exist(self):
        self.cursor.execute("SELECT type FROM documents WHERE type = ?",(self.type,))
        info = self.cursor.fetchone()
        return info != None

    def get_all_articles(self):
        self.cursor.execute(
            "SELECT filename FROM documents WHERE type=?", (self.type,))
        info = self.cursor.fetchall()
        filename = [item[0] for item in info]
        return filename