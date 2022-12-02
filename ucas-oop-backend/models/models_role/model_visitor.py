from .model_user import User

class Visitor(User):
    def __init__(self,username,password):
        super().__init__(username,password)
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        self.id,self.username,self.password = self.cursor.fetchone()