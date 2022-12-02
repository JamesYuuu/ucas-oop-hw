from sanic import Sanic

def add_config(app: Sanic):
    app.config.FALLBACK_ERROR_FORMAT = "json"
    app.config.DEBUG = False