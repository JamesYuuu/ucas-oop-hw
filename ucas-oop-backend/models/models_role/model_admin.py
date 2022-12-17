from .model_user import User

class Admin(User):

    document_per_type = 6
    type_per_page = 6

    def __init__(self,id):
        self.cursor.execute("SELECT username,password FROM users WHERE id = ?", (id,))
        username,password = self.cursor.fetchone()
        super().__init__(username,password)
    
    # return 6 documents for one page
    def get_documents(self,type):
        self.cursor.execute("SELECT filename FROM documents WHERE type=? ORDER BY id LIMIT ?",(type,self.document_per_type,))
        info = self.cursor.fetchall()
        filename = [item[0] for item in info]
        return filename

    # return 6 types for one page
    def get_types(self,page_num):
        offset = (int(page_num)-1) * self.type_per_page
        self.cursor.execute("SELECT DISTINCT type FROM documents ORDER BY id LIMIT ? OFFSET ?", (self.type_per_page,offset,))
        info = self.cursor.fetchall()
        types = [item[0] for item in info]
        return types

    def get_all_users(self):
        self.cursor.execute("SELECT username FROM users")
        info = self.cursor.fetchall()
        users = [item[0] for item in info]
        return users
        
    
    

