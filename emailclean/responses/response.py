class ResponseFailure:
    RESOURCE_ERROR = 'ResourceError'
    PARAMETERS_ERROR = 'ParametersError'
    SYSTEM_ERROR = 'SystemError'

    def __init__(self, type_, message):
        self.type = type_
        self.message = self.format_message(message)

    def format_message(self, msg):
        if isinstance(msg, Exception):
            return f'{msg.__class__.__name__}: {msg}'
        return msg

    @classmethod
    def build_from_invalid_request_object(cls, req):
        error_msg = req.errors
        return cls(cls.PARAMETERS_ERROR, error_msg)

    @property
    def value(self):
        return {'type': self.type, 'message': self.message}

    @classmethod
    def build_resource_error(cls, message: str):
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message: str):
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_system_error(cls, message: str):
        return cls(cls.SYSTEM_ERROR, message)

    def __bool__(self):
        return False

class ResponseSuccess:
    SUCCESS = 'Success'

    def __init__(self, value=None):
        self.value = value
        self.type = self.SUCCESS

    def __bool__(self):
        return True
