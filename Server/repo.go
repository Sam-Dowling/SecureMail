package main

import (
	"time"
	"math/rand"
	"sync"
)

var inboxes = make(map[int]Inbox)

var users = make(map[int]string)

var mutex = &sync.Mutex{}

func RepoFindInbox(mail_id int) Inbox {
	mutex.Lock()
	if i, ok := inboxes[mail_id]; ok {
		delete(inboxes, mail_id) // Clear inbox
		mutex.Unlock()
		return i
	}
	return Inbox{}
}

func RepoDeleteInbox(mail_id int) {
	mutex.Lock()
	delete(inboxes, mail_id)
	delete(users, mail_id)
	mutex.Unlock()
}

func RepoCreateMail(m Mail) Mail {
	mutex.Lock()
	inboxes[m.Header.Recipient] = append(inboxes[m.Header.Recipient], m)
	mutex.Unlock()
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
