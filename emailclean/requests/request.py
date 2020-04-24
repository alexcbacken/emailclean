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
    def __init__(self, type=None):
        self.type = type

    @classmethod
    def build(cls, type=None):
        invalid_req = InvalidRequestObject()
        if not type:
            err_message = f'type not specified try: {cls.accepted_req_types}'
            invalid_req.add_error('type', err_message)
            return invalid_req
        if type not in cls.accepted_req_types:
            err_message = f'type={type} is invalid. try: {cls.accepted_req_types}'
            invalid_req.add_error('type', err_message)
            return invalid_req
        return cls(type=type)


    def __bool__(self):
        return True


class DbGetReqObject(ValidRequestObject):

    accepted_req_types = ['sender', 'count', 'delete']


class ImapReqObject(ValidRequestObject):

    accepted_req_types = ['delete', 'all', 'connect']




    """"@ classmethod
    def build(cls,type=None):
        invalid_req = InvalidRequestObject
        if not type:
          invalid_req.add_error('type',
                                f'type not specified, try: {cls.accepted_req_types}')
        if type not in cls.accepted_req_types:
            invalid_req.add_error('type',
                                  f'type={cls.type} is invalid. try: {cls.accepted_req_types}') ')

        #return a list of uids from a DB connection
        #can be used to delete
        return None"""

    #invalid_req.add_error('Db', 'a database connection is required to return uids')



# build from a class method, allowing fo a missing db connection
# this will allow you to build a invalid request, if the db
# is missing. see rentomatic project. This has a test, started
# so ensure that test passes before moving on.

# Then contunine building you imap_use_case


