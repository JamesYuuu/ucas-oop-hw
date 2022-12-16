from sanic import Sanic
from controllers.controller_login import login
from controllers.controller_index import index
from controllers.controller_article import article

def add_routes(app: Sanic):
    app.add_route(login.as_view(), "/login")
    app.add_route(index.as_view(), "/index")
    app.add_route(article.as_view(), "/article")