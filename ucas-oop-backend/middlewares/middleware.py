from sanic.request import Request
from sanic import Sanic

from models.models_role.model_user import User
from models.models_role.model_admin import Admin
from models.models_role.model_visitor import Visitor

from models.models_document.model_document import Document
from models.models_document.model_type import Type

from exceptions.exception import *

def get_user(id):
    if id==1 :
        return Admin(id)
    else:
        return Visitor(id)

def extract_args(request: Request,str):
    if request.method in ['GET','DELETE']:
        return request.args.get(str)
    else:
        try:
            return request.json.get(str)
        except AttributeError:
            return None

def extract_user(request: Request):

    if request.uri_template == '/login':
        username = extract_args(request,'username')
        password = extract_args(request,'password')
        
        if not username or not password:
            raise BadRequestBody
        
        request.ctx.user = User(username,password)
    else:
        id = request.cookies.get('id')
        if not id:
            raise Unauthorized
        else:
            request.ctx.user = get_user(int(id))

def extract_document(request: Request):
    # TODO: Authority and Create new
    if request.uri_template =='/article':
        type = extract_args(request,'type')
        article = extract_args(request,'article')

        if (not article and request.method != 'GET'):
            raise BadRequestBody
        
        request.ctx.document = Document(article,type)

def extract_dashboard(request: Request):

    if request.uri_template == '/dashboard/type':
        type = extract_args(request,'name') 
        if type:
            request.ctx.type = Type(type)
        elif (request.method != 'GET'):
            raise BadRequestBody
    
    if request.uri_template == '/dashboard/article':
        article = extract_args(request,'name')
        if article:
            request.ctx.document = Document(article)
        elif (request.method != 'GET'):
            raise BadRequestBody


def add_middleware(app: Sanic):
    app.middleware('request')(extract_user)
    app.middleware('request')(extract_document)
    app.middleware('request')(extract_dashboard)