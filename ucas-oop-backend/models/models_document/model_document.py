from databases.database_base import Database

class Document(Database):

    def __init__(self,type = None,article = None):
        super().__init__()
        self.type = type
        self.article = article
    
    def get_all(self):
        self.cursor.execute("SELECT filename FROM documents WHERE type=?",(self.type,))
        info = self.cursor.fetchall()
        filename = [item[0] for item in info]
        return filename
    
    def get_text(self):
        pass