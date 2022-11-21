from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import json

class login(HTTPMethodView):
    
    def __init__(self):
        self.__app = Sanic.get_app("MarkItDown")
        self.__conn  = self.__app.ctx.db.conn
        self.__cursor = self.__app.ctx.db.cursor

    def get(self, request):
        username = request.args.get("username")
        password = request.args.get("password")
        if not username or not password:
            return json(status=400, body={"message": "Bad request"})
        self.__cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = self.__cursor.fetchone()
        if user:
            return json(status=200, body={"message": "Login successful"})
        else:
            return json(status=401, body={"message": "Login failed"})

    def post(self, request):
        username = request.json.get("username")
        password = request.json.get("password")
        if not username or not password:
            return json(status=400, body={"message": "Bad request"})
        self.__cursor.execute("select * from users where username = ?", (username,))
        user = self.__cursor.fetchone()
        if user:
            return json(status=409, body={"message": "User already exists"})
        self.__cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.__conn.commit()
        return json(status=200, body={"message": "success"})
    
    def put(self, request):
        username = request.json.get("username")
        password = request.json.get("password")
        self.__cursor.execute("select * from users where username = ?", (username,))
        user = self.__cursor.fetchone()
        if not user:
            return json(status=404, body={"message": "User not found"})
        self.__cursor.execute("UPDATE users SET password = ? WHERE username = ?", (password, username))
        self.__conn.commit()
        return json(status=200, body={"message": "Password updated"})
    
    def delete(self, request):
        username = request.json.get("username")
        self.__cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        self.__conn.commit()
        return json(status=200, body={"message": "User deleted"})