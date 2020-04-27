from emailclean.requests.request import InvalidRequestObject
from emailclean.responses import response as res
from emailclean.domain import email


class ImapFetchUseCase:

    def __init__(self, imap_client):
        self.imap_client = imap_client


    def execute(self, request):
        email_list = []
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            msg_list = self.imap_client.fetch(request.fields.get('name'))
            for msg in msg_list:
                email_obj = email.Email.from_dict(msg)
                email_list.append(email_obj)
        except Exception as e:
            # TODO: add key error handeling (.from_dict method),
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(email_list)


class ImapDeleteUseCase:
#(given list of uid and mailbox name)
    def __init__(self, imap_client):
        self.imap_client = imap_client

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            UIDs = request.fields.get('UIDs')
            mailbox = request.fields.get('name')
            result = self.imap_client.delete(mailbox, UIDs)
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


class ImapCreateNewFolderUseCase:
    def __init__(self, imap_client):
        self.imap_client = imap_client

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            folder = request.fields.get('name')
            result = self.imap_client.new_folder(folder)
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
            result = self.imap_client.mark_as(mailbox, flags, UIDs)
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

