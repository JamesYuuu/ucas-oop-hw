from .model_user import User

class Admin(User):
    def __init__(self,id):
        super().__init__()
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        self.id,self.username,self.password = self.cursor.fetchone()
    
    

