from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.request import Request

from exceptions.exception import *

from sanic_ext import openapi

from models.models_document.model_type import Type
from models.models_document.model_document import Document
from models.models_role.model_admin import Admin

from decorators.decorator import check_exist,authorized

from .controller_login import login


class dashboard_type(HTTPMethodView):
        
    @openapi.summary("This is used to get all types")
    def get(self, request: Request):
        result = Type.get_all_types()
        return json({'length':len(result),'result':result})
    
    @openapi.summary("This is used to create a new type")
    @authorized
    def post(self, request: Request):
        request.ctx.type.create_type()
        return json({'message':'create successful'})
    
    @openapi.summary("This is used to delete a type")
    @authorized
    def delete(self, request: Request):
        request.ctx.type.delete_type()
        return json({'message':'delete successful'})
    
    @openapi.summary("This is used to update a type")
    @authorized
    def put(self, request: Request):
        request.ctx.type.update_type(request.json.get('new_name'))
        return json({'message':'update successful'})

class dashboard_user(HTTPMethodView):

    @openapi.summary("This is used to get all users")
    @authorized
    def get(self, request: Request):
        result = Admin.get_all_users()
        return json({'length':len(result),'result':result})

    @openapi.summary("This is used to create a new user")
    @authorized
    def post(self, request: Request):
        username = request.json.get('name')
        Admin.create_user(username)
        return json({'message':'create successful'})
    
    @openapi.summary("This is used for change username")
    @check_exist('user')
    @authorized
    def put(self, request:Request):
        new_name = request.json.get('new_name')
        user = request.json.get('name')
        Admin.change_username(user,new_name)
        return json({"message": "Change username successful"})
    
    @openapi.summary("This is used for change password")
    @check_exist('user')
    @authorized
    def patch(self, request:Request):
        password = request.json.get('password')
        user = request.json.get('name')
        Admin.change_password(user,password)
        return json({"message": "Change password successful"})
    
    @openapi.summary("This is used for delete user")
    @check_exist('user')
    @authorized
    def delete(self, request:Request):
        user = request.args.get('name')
        Admin.delete_user(user)
        return json({"message": "Delete user successful"})

class dashboard_document(HTTPMethodView):
    
    @openapi.summary("This is used to get all documents")
    @authorized
    def get(self, request: Request):
        result = Document.get_all_documents()
        return json({'length':len(result),'result':result})

    @openapi.summary("This is used to create a document")
    @authorized
    @check_exist('document',is_exist=True)
    def post(self, request: Request):
        request.ctx.document.create_document()
        request.ctx.document.update_text("# Hello World")
        return json({'message':'create successful'})
    
    @openapi.summary("This is used to delete a document")
    @authorized
    @check_exist('document')
    def delete(self, request: Request):
        request.ctx.document.delete_document()
        return json({'message':'delete successful'})
    
    @openapi.summary("This is used to update a document")
    @authorized
    @check_exist('document')
    def put(self, request: Request):
        request.ctx.document.update_document(request.json.get('new_name'))
        return json({'message':'update successful'})
