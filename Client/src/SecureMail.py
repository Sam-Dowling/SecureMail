#!/usr/bin/env python3

import json
import requests
import pyotp
import os

SERVER_ADDRESS = '127.0.0.1:8080'


def get_http(args):
    return requests.get('http://{}/{}'.format(SERVER_ADDRESS, args)).json()


def post_http(args, post_data):
    return requests.post('http://{}/{}'.format(SERVER_ADDRESS, args), data=post_data)


class SecureMail:
    def __init__(self):
        self.inboxes = {}

    def Refresh_All(self):
        for i in self.inboxes:
            i.Refresh()

    def New_Inbox(self, alias):
        r = get_http('register')
        self.inboxes[alias] = Inbox(r['ID'], r['Secret'])

    def Inbox(self, alias):
        return self.inboxes[alias]

    def List_Inboxes(self):
        return list(self.inboxes.keys())

    def Save(self):
        for k, v in self.inboxes.items():
            with open('inboxes/{}.json'.format(k), 'w') as fp:
                json.dump(v.Dump(), fp)

    def Load(self):
        for filename in os.listdir('inboxes/'):
            with open('inboxes/{}'.format(filename)) as fp:
                data = json.load(fp)
                self.inboxes[os.path.splitext(filename)[0]] = Inbox(
                    data["inbox_id"], data["secret"], data["inbox"], data["sent"])


class Inbox:
    def __init__(self, inbox_id, secret, inbox=[], sent=[]):
        self.inbox_id = inbox_id
        self.totp = pyotp.TOTP(secret)
        self.inbox = inbox
        self.sent = sent

    def Refresh(self):
        new_messages = get_http('{}:{}'.format(self.inbox_id, self.totp.now()))
        self.inbox.extend(new_messages)

    def Inbox_ID(self):
        return self.inbox_id

    def Mail(self):
        return self.inbox

    def Sent(self):
        return self.sent

    def Send(self, recipient, message, file=None):
        data = {"Body": {"Text": "{}".format(message)}}
        if file:
            data["body"]["Attachment"] = {
                "File": '{}'.format(file), "Data": "BASE64 Data"}

        r = post_http('{}:{}/{}'.format(self.inbox_id,
                                        self.totp.now(), recipient), json.dumps(data))
        if r.status_code == 201:  # Created
            self.sent.append(r.json())

    def Dump(self):
        return {'inbox_id': self.inbox_id, 'secret': self.totp.secret,
                'inbox': self.inbox, 'sent': self.sent}


# # - USAGE -
# secure_mail = SecureMail()
#
# secure_mail.New_Inbox('bob')
# secure_mail.New_Inbox('tom')
#
# bob_id = secure_mail.Inbox('bob').Inbox_ID()
#
# secure_mail.Inbox('tom').Send(bob_id, "Hello Bob!")
#
# print(secure_mail.Inbox('tom').Sent())
#
# secure_mail.Inbox('bob').Refresh()
#
# print(secure_mail.Inbox('bob').Mail())
#
# secure_mail.Save()
#
# secure_mail.Load()
