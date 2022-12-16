from sanic.request import Request
from sanic import Sanic

from models.models_role.model_user import User
from models.models_role.model_admin import Admin
from models.models_role.model_visitor import Visitor

from models.models_document.model_document import Document

from exceptions.exception import *

def get_user(id):
    if id==1 :
        return Admin(id)
    else:
        return Visitor(id)

def get_document(type,article):
    return Document(type,article)

def extract_user(request: Request):

    if request.uri_template == '/login':
        username = request.args.get('username')
        password = request.args.get('password')
        
        if not username or not password:
            raise BadRequestBody
        
        request.ctx.user = User(username,password)
    else:
        id = request.cookies.get('id')
        if not id:
            raise Unauthorized
        else:
            request.ctx.user = get_user(int(id))
    
    # TODO: Authority and Create new
    if request.uri_template == '/article':
        type = request.args.get('type')
        article = request.args.get('article')
        request.ctx.document = get_document(type,article)


def add_middleware(app: Sanic):
    app.register_middleware(extract_user, 'request')