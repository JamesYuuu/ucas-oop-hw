from .model_user import User

class Visitor(User):
    def __init__(self,id):
        self.cursor.execute("SELECT username,password FROM users WHERE id = ?", (id,))
        username,password = self.cursor.fetchone()
        super().__init__(username,password)