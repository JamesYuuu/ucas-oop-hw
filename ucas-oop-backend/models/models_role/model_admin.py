from .model_user import User

class Admin(User):

    document_per_type = 6
    type_per_page = 6
    default_password = 123456

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

    @classmethod
    def get_all_users(cls):
        cls.cursor.execute("SELECT username FROM users")
        info = cls.cursor.fetchall()
        users = [item[0] for item in info]
        return users

    # use for delete
    @classmethod
    def delete_user(cls,username):
        cls.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        cls.conn.commit()
    
    # use for update password
    @classmethod
    def change_password(cls,password,username):
        cls.cursor.execute("UPDATE users SET password = ? WHERE username = ?", (password, username))
        cls.conn.commit()
    
    # use for reset password default password = 123456
    @classmethod
    def reset_password(cls,username):

        cls.cursor.execute("UPDATE users SET password = ? WHERE username = ?", (cls.default_password, username))
        cls.conn.commit()

    @classmethod
    def create_user(cls,username):
        cls.cursor.execute("INSERT INTO users (username,password) VALUES (?,?)",(username,cls.default_password,))
        cls.conn.commit()

    @classmethod
    def change_username(cls,username,new_name):
        cls.cursor.execute("UPDATE users SET username = ? WHERE username = ?", (new_name, username))
        cls.conn.commit()
        