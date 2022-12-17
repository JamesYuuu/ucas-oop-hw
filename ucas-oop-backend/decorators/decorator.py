
from functools import wraps

from exceptions.exception import *

class check_exist(object):

    def __init__(self,item_name,is_exist=False):
        self.item_name = item_name
        self.is_exist = is_exist

    def __call__(self,func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            result = getattr(args[1].ctx,self.item_name).exist()
            if not result and not self.is_exist:
                raise NotFound
            if result and self.is_exist:
                raise AlreadyExists
            return func(*args, **kwargs)
        return decorated_function

def authorized(func):
    @wraps(func)
    def decorated_func(*args,**kwargs):
        if args[1].ctx.user.__class__.__name__ != 'Admin':
            raise Unauthorized
        return func(*args,**kwargs)
    return decorated_func