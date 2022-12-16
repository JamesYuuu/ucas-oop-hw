from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.request import Request

from exceptions.exception import *

class article(HTTPMethodView):
    
    '''
    @param article
    @param type
    if article is null we return all articles from type
    '''
    def get(self, request: Request):
        document = request.ctx.document
        if not document.type:
            return json('# Hello World')
        if not document.article:
            result=document.get_all()
            return json({'length':len(result),'result':result})
        else:
            text = document.get_text()
            if not text:
                raise FileNotFound
            else:
                return json(document.get_text())

    def post(self, request: Request):
        document = request.ctx.document
        document.create_document()
        document.update_text(request.json.get('text'))
        return json({'message':'create successful'})
    
    def put(self, request: Request):
        document = request.ctx.document
        document.update_text(request.json.get('text'))
        return json({'message':'save successful'})

    