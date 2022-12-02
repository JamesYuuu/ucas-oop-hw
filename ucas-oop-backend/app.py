from sanic import Sanic
from sanic_ext import Extend

from routes.route import add_routes
from middlewares.middleware import add_middleware
from config.config import add_config

app = Sanic("MarkItDown")
Extend(app)

add_routes(app)
add_middleware(app)

add_config(app)

if __name__ == "__main__":
    app.run()
