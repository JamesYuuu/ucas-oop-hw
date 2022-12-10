from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.request import Request

class index(HTTPMethodView):
    
    def get(self,request: Request):
        user = request.ctx.user
        page_num = request.args.get('page')
        return json({'filename': user.get_documents(page_num)})