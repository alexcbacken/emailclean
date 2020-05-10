import email

"""
The decision has been made to keep the date as a string instead of a datetime obj. This is
due to datetime's inability to be serialised, and the potential differing string formats from different
servers. In the future this could be implemented using regex
"""

class Email():
    def __init__(self, uid, sender, date, subject, receiver, read, flags):
        self.uid = uid
        self.sender = sender
        self.date = date
        self.subject = subject
        self.receiver = receiver
        self.read = read
        self.flags = flags


    @classmethod
    def from_dict(cls, dict):
        cls.uid = dict["uid"]
        cls.sender = dict["sender"]
        cls.date = dict["date"]
        cls.subject = dict["subject"]
        cls.receiver = dict["receiver"]
        cls.read = dict["read"]
        cls.flags = dict["flags"]
        return cls

    def as_msg_obj(self):
        raise NotImplementedError('you need to write this!!')





