package main

import "time"

type Mail struct {
	Header Header
	Body Body
}

type Header struct{
	Sender int
	Recipient int
	Timestamp time.Time
}

type Attachment struct{
	File string
	Data string
}

type Body struct{
	Encrypted bool
	Text string
	Attachment Attachment
}

type User struct{
	ID int
	Secret string
}

type Inbox []Mail
