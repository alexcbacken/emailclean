from emailclean.domain.email import Email

class InvalidRequestObject:
    def __init__(self):
        self.errors = {}

    def add_error(self, error:tuple):
        self.errors.update({'parameter': error[0], 'problem': error[1]})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False

class ValidRequestObject:

    # you will need a @class method
    # def from dict in here, so this can become the base class
    # for all your requests
    accepted_req = {}

    def __init__(self, **fields):
        self.fields = fields

    @classmethod
    def build(cls, **fields):
        invalid_req = InvalidRequestObject()
        if hasattr(cls, "accepted_req"):
            validated = cls.validate_fields(fields)
            if not validated[0]:
                err_message = validated[1]
                invalid_req.add_error(err_message)
                return invalid_req

        return cls(**fields)

    @classmethod
    def validate_fields(cls, adict):
        validation = True
        error_msg = ""
        if adict:
            try:
                for key, value in adict.items():
                    if not isinstance(value, cls.accepted_req.get(key)):
                        validation = False
                        error_msg = (key, f"incorrect type try {cls.accepted_req[key]}")
            except KeyError as e:
                validation = False
                error_msg = (key, "incorrect arg value")
            except TypeError as e:
                validation = False
                error_msg = (key, "incorrect arg value")

        return (validation, error_msg)

    def __bool__(self):
        return True

class DbRequestObject(ValidRequestObject):

        # should be an iterator containing these items
        accepted_req = {"msgs": list,
                        "flags": list,
                        "UIDs": list,
                        "name": str,
                        }

class DbGetReqObject(DbRequestObject):

    # a accepted kwarg dict. key word is the key. accepted
    # values are accepted values
    accepted_req = {'get': ['sender', 'all', 'delete'],}

    #TODO change to return custom error msg
    @classmethod
    def validate_fields(cls, adict):
        validation = True
        error_msg = ""
        if not adict:
            validation = False
            error_msg = ("kwargs", "none passed")
        for key in adict:
            try:
                if adict[key] not in cls.accepted_req[key]:
                    validation = False
                    error_msg = (adict[key], "not an expected argument")
            except [KeyError, TypeError] as e:
                validation = False
                error_msg = (key, str(e))
        return (validation, error_msg)

class ImapReqObject(ValidRequestObject):

    accepted_req = {'name': str,
                    'UIDs': list,
                    'flags': str,
                    "conn": dict}






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


