package main

import "net/http"

type Route struct {
	Name        string
	Method      string
	Pattern     string
	HandlerFunc http.HandlerFunc
}

type Routes []Route

var routes = Routes{
	Route{
		"Register",
		"GET",
		"/register",
		RegisterGet,
	},
	Route{
		"Inbox Request",
		"GET",
		"/{mail_id}:{totp_token}",
		InboxGet,
	},
	Route{
		"Mail Sent",
		"POST",
		"/{sender_id}:{totp_token}/{recipient_id}",
		MailPost,
	},
}
