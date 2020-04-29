import pytest
from emailclean.servers import imap_server
pytestmark = pytest.mark.imap_server

"""
test connect method
connects to imap server, downloads messages. creates db.

test delete method

test imap all method



"""

# look to see how renotmatic, handles its integeration test setup
# yours just returns a result tupal. but is actuality you probablty
# want a localmail server and imap client running so you can send them
# your requests. The only thing fake will be that the msgs are coming
# from local mail, not googlemail. i  guess, check at which point
# the actual code gets mocked. I think it it esentially only the
# imablib.IMAP4(host=, port=) that will have to be patched in.

def test_Imap_Server_connects():


    pass
"""
msg_list = self.imap_client.fetch(request.fields.get('name'))

result = self.imap_client.delete(mailbox, UIDs)

result = self.imap_client.new_mb(mailbox)

result = self.imap_client.new_folder(folder)

result = self.imap_client.mark_as(mailbox, flags, UIDs)

result = self.imap_client.move_to(mailbox, UIDs)
"""
