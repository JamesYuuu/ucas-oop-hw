from databases.database_base import Database
import datetime

from functools import wraps

def renew_edit_time(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        args[0].update_edit_time()
        return f(*args, **kwargs)
    return decorated_function


class Document(Database):

    def __init__(self, type, article):
        self.type = type
        self.article = article

    @staticmethod
    def get_time():
        return datetime.datetime.now().strftime('%Y-%m-%d')
    
    def update_edit_time(self):
        current_time = self.get_time()
        self.cursor.execute(
            "UPDATE documents SET edit_time = ? WHERE filename = ?", (current_time, self.article))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute(
            "SELECT filename FROM documents WHERE type=?", (self.type,))
        info = self.cursor.fetchall()
        filename = [item[0] for item in info]
        return filename

    def get_text(self):
        try:
            with open('storage/'+self.type+'/'+self.article+'.md', 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            text = '# Hello World'
        return text

    def create_document(self):
        current_time = self.get_time()
        self.cursor.execute("INSERT INTO documents (type, filename , create_time,edit_time) VALUES (?, ?, ?,?)",
                            (self.type, self.article, current_time, current_time))
        self.conn.commit()
    
    @renew_edit_time
    def update_text(self, text):
        with open('storage/'+self.type+'/'+self.article+'.md', 'w+', encoding='utf-8') as f:
            f.write(text)

    @classmethod
    def get_all_documents(cls):
        cls.cursor.execute("SELECT filename FROM documents")
        info = cls.cursor.fetchall()
        filename = [item[0] for item in info]
        return filename
    
    def delete_document(self):
        self.cursor.execute("DELETE FROM documents WHERE filename = ?",(self.article,))
        self.conn.commit()

    @renew_edit_time
    def update_document(self, new_name):
        self.cursor.execute("UPDATE documents SET filename = ? WHERE filename = ?",(self.article,new_name,))
        self.conn.commit()
