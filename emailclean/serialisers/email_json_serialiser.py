import json


class EmailJsonEncoder(json.JSONEncoder):

    # whats this? it just returns a dict!
    # yes it does, but not to the caller. You have overridden the
    # 'default' method in the json.JSONEncoder class.
    # it converts a non-serilisable object into a serilisable object
    # which then gets serilised. The type emai that you sent is not a
    # serialisable object. ONLY beacuse the date class is not directly
    # serialisable. so you send the object, convert the date in to a
    # string. then the JSONEncoder encodes that. (i think int is also not serialisable)
    def default(self, o):
        try:
            to_serialise = {
                "uid": o.uid,
                "sender": o.sender,
                "date": o.date,
                "subject": o.subject,
                "receiver": o.receiver,
                "read": o.read,
                "flags": o.flags,
                "mailbox": o.mailbox,
            }
            return to_serialise
        except AttributeError:
            return super().default(o)
    """There could be other ways of doing this ie you could keep
        the date as a string. then you would
        have an email object that could be seriliased. so their would
        be no need to override this method"""
