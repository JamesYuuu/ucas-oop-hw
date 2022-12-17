from sanic import Sanic,Blueprint
from sanic_ext import Extend

from routes.route import add_routes
from middlewares.middleware import add_middleware
from config.config import add_config

app = Sanic("MarkItDown")
Extend(app)

bp = Blueprint('dashboard',url_prefix='/dashboard')
app.blueprint(bp)

add_routes(app,bp)
add_middleware(app)

add_config(app)

if __name__ == "__main__":
    app.run(dev=True)
