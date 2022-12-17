from databases.database_base import Database
import os
import shutil
import datetime

class Type(Database):

    default_article = 'README'

    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def get_time():
        return datetime.datetime.now().strftime('%Y-%m-%d')

    @classmethod
    def get_all_types(cls):
        cls.cursor.execute("SELECT DISTINCT type FROM documents")
        info = cls.cursor.fetchall()
        types = [item[0] for item in info]
        return types
    
    def create_type(self):
        current_time = self.get_time()
        self.cursor.execute("INSERT INTO documents (type, filename , create_time,edit_time) VALUES (?, ?, ?,?)",
                            (self.type, self.default_article, current_time, current_time))
        self.conn.commit()
        os.mkdir('storage/'+self.type)
    
    def update_type(self,new_name):
        self.cursor.execute("UPDATE documents SET type = ? WHERE type = ?",(new_name,self.type,))
        self.conn.commit()

    def delete_type(self):
        self.cursor.execute("DELETE FROM documents WHERE type = ?",(self.type,))
        self.conn.commit()
        shutil.rmtree('storage/'+self.type)

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