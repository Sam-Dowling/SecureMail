package main

import (
	"time"
	"math/rand"
)

var inboxes = make(map[int]Inbox)

var users = make(map[int]string)

// Give us some seed data
// func init() {
//
// 	user1 := RepoRegister(GenNewSecret())
// 	user2 := RepoRegister(GenNewSecret())
//
// 	fmt.Println(user1)
//
// 	RepoCreateMail(Mail{
// 		Header: Header{user2.ID, user1.ID, time.Now()},
// 		Body:   Body{"Text of email goes here", Attachment{"img.jpg", "base64 data"}},
// 	})
// }

func RepoFindInbox(mail_id int) Inbox {
	if i, ok := inboxes[mail_id]; ok {
		delete(inboxes, mail_id) // Clear inbox
		return i
	}
	return Inbox{}
}

func RepoCreateMail(m Mail) Mail {
	inboxes[m.Header.Recipient] = append(inboxes[m.Header.Recipient], m)
	return m
}

func RepoRegister(secret string) User {
	id := newID()
	for users[id] != ""{
		id = newID()
	}
	users[id] = secret
	return User{id, secret}
}

func RepoGetUser(id int) string{
	return users[id]
}

func newID() int {
	rand.Seed(time.Now().UTC().UnixNano())
	return 1000000000 + rand.Intn(9999999999-1000000000)
}
