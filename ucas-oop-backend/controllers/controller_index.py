from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.request import Request

class index(HTTPMethodView):
    
    def get(self,request: Request):
        user = request.ctx.user
        page_num = request.args.get('page')
        if not page_num:
            return json({'page_num':user.get_page_num()})
        types = user.get_types(page_num)
        result = [{'type': types[index],'article': user.get_documents(types[index])} for index in range(len(types))]
        return json({'length':len(result),'result':result})