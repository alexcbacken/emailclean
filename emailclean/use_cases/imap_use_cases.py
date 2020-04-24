from emailclean.requests.request import InvalidRequestObject
from emailclean.responses import response as res
from emailclean.domain import email


class ImapDeleteFromDbUseCase:

    def __init__(self, imap_client, db):
        self.imap_client = imap_client
        self.db = db

    def execute(self, request):
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            result = self.imap_client.delete(self.db.get_delete_list())
        except Exception as e:
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(result)
# take db del list and delete mails from mail box


class ImapConnectUseCase:

    def __init__(self, imap_client, db):
        self.imap_client = imap_client
        self.db = db

    def execute(self, request):
        email_list=[]
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            msg_list = self.imap_client.connect()
            for msg in msg_list:
                email_obj = email.Email.from_dict(msg)
                email_list.append(email_obj)
            self.db.write(email_list)
            result = f'inbox added to db, db length is {self.db.get(type="count")}'
        except Exception as e:
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(result)
# connect to inbox and download all messages.


class ImapAllUseCase:
    def __init__(self, imap_client, mailbox):
        self.imap_client = imap_client
        self.mailbox = mailbox


    def execute(self, request):
        email_list=[]
        if type(request) is InvalidRequestObject:
            return res.ResponseFailure.build_from_invalid_request_object(request)
        try:
            msg_list = self.imap_client.all(self.mailbox)
            for msg in msg_list:
                email_obj = email.Email.from_dict(msg)
                email_list.append(email_obj)

        except Exception as e:
            return res.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")
        return res.ResponseSuccess(email_list)

