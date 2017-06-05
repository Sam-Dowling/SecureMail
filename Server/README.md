# SecureMail Server

A Secure, Anonymous messaging API Server.

SSL should be enabled and encryption enabled in the client.

## Getting Started

Compile the Project with ``Go build``

Run the SecureMail Executable

### Installing

Install [GoLang](https://golang.org/)

Get the required packages
```
$ cd SecureMail/Server
$ go get github.com/pquerna/otp
$ go get github.com/gorilla/mux
```

## Usage

### Registering
```
GET 127.0.0.1:8080/register
=> 
{
  "ID": 9433248649,
  "Secret": "VXHCRBUG7BQTC7PY"
}
```
- The ID is used in requesting the inbox and sending messages
- The Secret is used to generate TOTP tokens used to authenticate the user

### Request Inbox
```
GET 127.0.0.1:8080/{ID}:{TOTP_Token}
=>
{
  "Header": {
    "Sender": 8714731264,
    "Recipient": 9433248649,
    "Timestamp": "0001-01-01T00:00:00Z"
  },
  "Body": {
    "Encrypted": false,
    "Text": "Text of message goes here",
    "Attachment": {
      "File": "cat.jpg",
      "Data": "<base64 data>"
    }
  }
}
```
- The TOTP_Token cannot be used for replay attacks
- Once an inbox has been accessed; the inbox is cleared.
- It is the clients responsibility to store the messages once retrieved from the server.

### Send Message
```
POST 127.0.0.1:8080/{Sender_ID}:{TOTP_Token}/{Recipient_ID}
->
{
  "Body": {
    "Encrypted": false,
    "Text": "Text of message goes here",
    "Attachment": {
      "File": "cat.jpg",
      "Data": "<base64 data>"
    }
  }
}
```
- Post the "Body" section of the message to the above endpoint
- "Attachment" is optional.
- If encryption is used, "Text" and the attachment "Data" should be encrypted with AES by the client.
- If the message is sent successfully; the message object will be returned with the "Header" populated.
- the TOTP_Token must be generated and sent like before.
