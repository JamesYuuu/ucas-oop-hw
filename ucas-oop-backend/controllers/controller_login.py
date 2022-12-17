from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.request import Request

from sanic_ext import openapi

from exceptions.exception import *

from functools import wraps

from decorators.decorator import check_exist

class login(HTTPMethodView):
    
    @openapi.summary("This is used for login")
    @check_exist('user')
    def get(self, request:Request):
        response = json({"message": "Login successful"})
        response.cookies["id"] = str(request.ctx.user.id)
        return response

    @openapi.summary("This is used for register")
    @check_exist(item_name='user',is_exist=True)
    def post(self, request:Request):
        request.ctx.user.create_user()
        return json({"message": "Register successful"})
