from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.request import Request

from exceptions.exception import *

class login(HTTPMethodView):
    
    def get(self, request:Request):
        is_exist = request.ctx.user.login_user()
        if is_exist:
            response = json({"message": "Login successful"})
            response.cookies["id"] = str(request.ctx.user.id)
            return response
        else:
            raise UserNotFound

    def post(self, request:Request):

        if request.ctx.user.check_username():
            raise UserAlreadyExists
        
        request.ctx.user.create_user()
        return json({"message": "Register successful"})