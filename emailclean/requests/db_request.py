class InvalidRequestObject:
    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False

class ValidRequestObject:

    # you will need a @class method
    # def from dict in here, so this can become the base class
    # for all your requests

    def __bool__(self):
        return True

class DbGetReqObject(ValidRequestObject):

    def __init__(self, type=None):
        self.type = type


