from databases.database_base import Database

class User(Database):

    def __init__(self,username = None,password = None):
        super().__init__()
        self.username = username
        self.password = password
    
    # use for register
    def create_user(self):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.username, self.password))
        self.conn.commit()

    # use for login
    def login_user(self):
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (self.username, self.password))
        self.id,*_= self.cursor.fetchone()
        if self.id:
            return True
        else:
            return False
    
    # use for update password
    def change_password(self):
        self.cursor.execute("UPDATE users SET password = ? WHERE username = ?", (self.password, self.username))
        self.conn.commit()
    
    # use for reset password default password = 123456
    def reset_password(self):
        default_password = 123456
        self.cursor.execute("UPDATE users SET password = ? WHERE username = ?", (default_password, self.username))
        self.conn.commit()

    # check if username is exist
    def check_username(self):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (self.username,))
        user = self.cursor.fetchone()
        if user:
            return True
        else:
            return False

