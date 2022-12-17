
from sanic.exceptions import SanicException

class NotFound(SanicException):
    status_code = 404
    message = "Not found"
    quiet = True

class AlreadyExists(SanicException):
    status_code = 409
    message = "Already exists"
    quiet = True

class BadRequestBody(SanicException):
    status_code = 400
    message = "Bad request"
    quiet = True

class Unauthorized(SanicException):
    status_code = 401
    message = "Unauthorized"
    quiet = True
