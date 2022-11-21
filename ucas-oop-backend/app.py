from sanic import Sanic
from db.db_base import Database
from route import add_routes
from sanic_ext import Extend

app = Sanic("MarkItDown")
app.ctx.db = Database()
Extend(app)
add_routes()

if __name__ == "__main__":
    app.run()
