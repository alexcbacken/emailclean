from datetime import datetime
import email

class Email():
    def __init__(self, uid, sender, date, subject, receiver):
        self.uid = uid
        self.sender = sender
        self.date = self.date_to_date_obj(date)
        self.subject = subject
        self.receiver = receiver

    def date_to_datetime(self, date):
        if isinstance(date, str):
            return datetime.strptime(date[0:16], "%a, %d %b %Y").date()
        else:
            return date

    @classmethod
    def from_dict(cls, dict):
        cls.uid = dict["uid"]
        cls.sender = dict["sender"]
        cls.date = dict["date"]
        cls.subject = dict["subject"]
        cls.receiver = dict["receiver"]
        return cls



