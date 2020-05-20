from emailclean.requests.request import InvalidRequestObject
from emailclean.responses import response as res
from emailclean.domain import email


class DbCreateUseCase:

    def __init__(self, Db):
        self.db = Db


    def execute(self, request):

        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            email_list = request.fields.get('msgs')
            result = self.db.create(email_list)
        except Exception as e:
            # TODO: add key error handeling (.from_dict method),
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(result)


class DbMarkAsUseCase:

    def __init__(self, Db):
        self.db = Db

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            UIDs = request.fields.get('UIDs')
            flags = request.fields.get('flags')
            result = self.db.mark_as(UIDs, flags)
        except Exception as e:
            # TODO: add key error handeling (.from_dict method),
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(result)

class DbGetUseCase:

    def __init__(self, Db):
        self.db = Db

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            get_type = request.fields.get('get')
            result = self.db.get(get=get_type)
        except Exception as e:
            # TODO: add key error handeling (.from_dict method),
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(result)


class DbDeleteDbUseCase:
    def __init__(self, Db):
        self.db = Db

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            result = self.db.delete()
        except Exception as e:
            # TODO: add key error handeling (.from_dict method),
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(result)


"""
class SenderListUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            email_list = self.repo.get(type=request.type)
        except Exception as e:
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(email_list)

class DeleteListUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            email_list = self.repo.get(type=request.type)
        except Exception as e:
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(email_list)

class CountUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            email_list = self.repo.get(type=request.type)
        except Exception as e:
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(email_list)


"""





