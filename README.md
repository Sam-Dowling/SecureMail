# SecureMail

A Secure, Anonymous Messaging service and Client.

The [Server](Server) is written in GoLang and provides an easy to use API for interacting with inboxes and user management.

The server is extremely lightweight with features such as
- In-memory datastore.
- POP3 like functionality where inboxes are flushed once read by the client.
- TOTP tokens used for authenticating users.
- Inboxes are easily disposable and very lightweight.

The [Client](Client) is written in Python with GTK3.

## Installing & Usage

See [Server](Server) and [Client](Client) folders for detailed installation and usage instructions.

### Collaborators
- [Luke Bluett](https://github.com/LukeBluett)
- [Sam Dowling](https://samdowling.com)
- [Johnjoe Landers](https://github.com/johnjoelanders)

### Note

While efforts have been made to ensure the security and stability of this project; bug-free code cannot be ensured.

This is a 'pet' project and extensive testing is not going to be done.

Therefore in a situation where security is a very real concern; a more mature solution should be used.
