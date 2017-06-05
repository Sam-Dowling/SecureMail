#!/usr/bin/env python3

import json
import requests
import pyotp

SERVER_ADDRESS = '127.0.0.1:8080'


class SecureMail:
    def __init__(self):
        self.inboxes = {}

    def RefreshAll(self):
        for i in self.inboxes:
            i.Refresh()

    def NewInbox(self, alias):
        r = get_http('register')
        self.inboxes[alias] = Inbox(r['ID'], r['Secret'])

    def Inbox(self, alias):
        return self.inboxes[alias]


class Inbox:
    def __init__(self, inbox_id, secret):
        self.inbox_id = inbox_id
        self.totp = pyotp.TOTP(secret)
        self.inbox = []
        self.sent = []

    def Refresh(self):
        new_messages = get_http('{}:{}'.format(self.inbox_id, self.totp.now()))
        self.inbox.extend(new_messages)

    def InboxID(self):
        return self.inbox_id

    def Mail(self):
        return self.inbox

    def Sent(self):
        return self.sent

    def Send(self, recipient, message):
        data = json.dumps({"Body": {"Text": "{}".format(message), "Attachment": {
                          "File": "cat.jpg", "Data": "base64 data"}}})
        r = post_http('{}:{}/{}'.format(self.inbox_id,
                                        self.totp.now(), recipient), data)
        if r.status_code == 201:  # Created
            self.sent.append(r.json())


def get_http(args):
    return requests.get('http://{}/{}'.format(SERVER_ADDRESS, args)).json()


def post_http(args, post_data):
    return requests.post('http://{}/{}'.format(SERVER_ADDRESS, args), data=post_data)

# - USAGE -
# secure_mail = SecureMail()
#
# secure_mail.NewInbox('bob')
# secure_mail.NewInbox('tom')
#
# bob_id = secure_mail.Inbox('bob').InboxID()
#
# secure_mail.Inbox('tom').Send(bob_id, "Hello Bob!")
#
# print(secure_mail.Inbox('tom').Sent())
#
# secure_mail.Inbox('bob').Refresh()
#
# print(secure_mail.Inbox('bob').Mail())
