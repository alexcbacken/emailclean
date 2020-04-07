import email

"""
The decision has been made to keep the date as a string instead of a datetime obj. This is
due to datetime's inability to be serialised, and the differing string formats from different
servers. In the future this could be implemented using regex
"""

class Email():
    def __init__(self, uid, sender, date, subject, receiver):
        self.uid = uid
        self.sender = sender
        self.date = date
        self.subject = subject
        self.receiver = receiver

    @classmethod
    def from_dict(cls, dict):
        cls.uid = dict["uid"]
        cls.sender = dict["sender"]
        cls.date = dict["date"]
        cls.subject = dict["subject"]
        cls.receiver = dict["receiver"]
        return cls



