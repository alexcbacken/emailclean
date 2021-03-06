from emailclean.requests.request import InvalidRequestObject
from emailclean.responses import response as res
from emailclean.domain import email
from emailclean.servers.imap_server import ImapClient

class ImapConnectUseCase:

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            imap_client = ImapClient.connect(request.fields.get('conn'))
        except Exception as e:
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(imap_client)

class ImapCloseUseCase:

    def __init__(self, imap_client):
        self.imap_client = imap_client


    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            self.imap_client.close()
        except Exception as e:
            # TODO: add key error handeling (.from_dict method),
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess()

class ImapFetchUseCase:

    def __init__(self, imap_client):
        self.imap_client = imap_client


    def execute(self, request):
        """
        executes a fetch command on the imap_client
        :param request: emailclean.requests.ImapReqObject
        :return: list of EMail objects (emailclean.domain.email.Email)
        """
        email_list = []
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            msg_list = self.imap_client.fetch(request.fields.get('name'))
        except Exception as e:
            # TODO: add key error handeling (.from_dict method),
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(msg_list)


class ImapDeleteUseCase:

    def __init__(self, imap_client):
        self.imap_client = imap_client

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            mailbox = request.fields.get('name')
            result = self.imap_client.delete(mailbox)
        except Exception as e:
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(result)



class ImapCreateNewMailboxUseCase:

    def __init__(self, imap_client):
        self.imap_client = imap_client

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            mailbox = request.fields.get('name')
            result = self.imap_client.new_mb(mailbox)
        except Exception as e:
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(result)

class ImapMarkAsUseCase:
    def __init__(self, imap_client):
        self.imap_client = imap_client

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            mailbox = request.fields.get('name')
            flags = request.fields.get('flags')
            UIDs = request.fields.get('UIDs')
            result = self.imap_client.mark_as(mailbox, UIDs, flags)
        except Exception as e:
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(result)

class ImapMoveToUseCase:
    def __init__(self, imap_client):
        self.imap_client = imap_client

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            # mailbox is the destination. the email will be objects in the db, so
            # wont have a mailbox source as such.
            mailbox = request.fields.get('name')
            UIDs = request.fields.get('UIDs')

            result = self.imap_client.move_to(mailbox, UIDs)
        except Exception as e:
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(result)

