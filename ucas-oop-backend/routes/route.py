from sanic import Sanic
from controllers.controller_login import login

def add_routes(app: Sanic):
    app.add_route(login.as_view(), "/login")