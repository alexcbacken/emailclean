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
    def __init__(self, **fields):
        self.fields = fields

    @classmethod
    def build(cls, **fields):
        invalid_req = InvalidRequestObject()
        if hasattr(cls, "accepted_req"):
            if not cls.validate_fields(fields):
                err_message = f'invalid args: {[x[0] + "=" +str(x[1]) for x in fields.items()]}  ' \
                              f'try: {[str(x[0]) + "="+str(x[1]) for x in cls.accepted_req.items()]}'
                invalid_req.add_error('invalid args', err_message)
                return invalid_req

        return cls(**fields)

    def validate_fields(self, adict):
        pass


    def __bool__(self):
        return True


class DbGetReqObject(ValidRequestObject):

    # a accepted kwarg dict. key word is the key. accepted
    # values are accepted values
    accepted_req = {'type': ['sender', 'all', 'delete']}

    @classmethod
    def validate_fields(cls, adict):
        if not adict:
            return False
        for key in adict:
            try:
                if adict[key] not in cls.accepted_req[key]:
                    return False
            except KeyError:
                return False
        return True







class ImapReqObject(ValidRequestObject):

    accepted_req = {'name': str,
                    'UIDs': list,
                    'flags': list}

    @classmethod
    def validate_fields(cls, adict):
        result = False
        try:
            for key in adict:
                #check name is correct type, with a length
                if (isinstance(adict[key], cls.accepted_req[key]) and bool(len(adict[key]))):
                    result = True
        except KeyError:
            result = False

        return result



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


