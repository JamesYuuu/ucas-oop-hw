from .model_user import User
from sanic.log import logger

class Admin(User):
    def __init__(self,id):
        super().__init__()
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        self.id,self.username,self.password = self.cursor.fetchone()
    
    # return 10 filenames for one page
    def get_documents(self,page_num):
        offset = int(page_num) * 10 - 10
        self.cursor.execute("SELECT * FROM documents ORDER BY id DESC LIMIT 10 OFFSET ?", (offset,))
        info = self.cursor.fetchall()
        filename = [item[1] for item in info]
        return filename 
        
    
    

