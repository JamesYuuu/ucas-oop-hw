
from sanic.exceptions import SanicException

class UserNotFound(SanicException):
    status_code = 404
    message = "User not found"
    quiet = True

class UserAlreadyExists(SanicException):
    status_code = 409
    message = "User already exists"
    quiet = True

class BadRequestBody(SanicException):
    status_code = 400
    message = "Bad request"
    quiet = True

class Unauthorized(SanicException):
    status_code = 401
    message = "Unauthorized"
    quiet = True

class FileNotFoud(SanicException):
    status_code = 404
    message = "File not found"
    quiet = True