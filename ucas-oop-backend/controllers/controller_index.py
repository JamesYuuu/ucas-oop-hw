from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.request import Request

from sanic_ext import openapi

class index(HTTPMethodView):
    
    @openapi.description('We return 6 types per page and 6 documents per type')
    @openapi.summary("This is used to get some informations")
    def get(self,request: Request):
        user = request.ctx.user
        page_num = request.args.get('page') if request.args.get('page') else 1
        types = user.get_types(page_num)
        result = [{'type': types[index],'article': user.get_documents(types[index])} for index in range(len(types))]
        return json({'length':len(result),'result':result})