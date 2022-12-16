from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.request import Request

from exceptions.exception import *

class article(HTTPMethodView):
    
    def get(self, request: Request):
        document = request.ctx.document
        if not document.article:
            result=document.get_all()
            return json({'length':len(result),'result':result})
        else:
            return json(document.get_text())