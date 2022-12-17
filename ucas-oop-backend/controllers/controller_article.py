from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.request import Request

from exceptions.exception import *

from sanic_ext import openapi

class article(HTTPMethodView):
    
    @openapi.description('''
        if document.article is empty we return all articles of the type
        if document.article is not empty we return the text of the article    
    ''')
    @openapi.summary("This is used to get some informations")
    def get(self, request: Request):
        document = request.ctx.document
        if not document.article:
            result=document.get_all_articles()
            return json({'length':len(result),'result':result})
        else:
            text = document.get_text()
            return json(document.get_text())

    @openapi.summary("This is used to create a new document")
    def post(self, request: Request):
        document = request.ctx.document
        document.create_document()
        document.update_text(request.json.get('text'))
        return json({'message':'create successful'})
    
    @openapi.summary("This is used to update a document")
    def put(self, request: Request):
        document = request.ctx.document
        document.update_text(request.json.get('text'))
        return json({'message':'save successful'})

    