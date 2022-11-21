from sanic import Sanic
from routes.view_login import login

def add_routes():
    app = Sanic.get_app("MarkItDown")
    app.add_route(login.as_view(), "/login")