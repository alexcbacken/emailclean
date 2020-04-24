from emailclean.requests.request import InvalidRequestObject
from emailclean.responses import response as res


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








