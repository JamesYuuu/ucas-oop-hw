from sanic import Sanic,Blueprint
from controllers.controller_login import login
from controllers.controller_index import index
from controllers.controller_article import article

from controllers.controller_dashboard import dashboard_type,dashboard_document,dashboard_user

def add_routes(app: Sanic, bp:Blueprint):
    app.add_route(login.as_view(), "/login")
    app.add_route(index.as_view(), "/index")
    app.add_route(article.as_view(), "/article")

    bp.add_route(dashboard_type.as_view(),'/type')
    bp.add_route(dashboard_document.as_view(),'/article')
    bp.add_route(dashboard_user.as_view(),'/user')
