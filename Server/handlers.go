package main

import (
	"encoding/json"
	"io"
	"io/ioutil"
	"net/http"
	"strconv"
	"time"

	"github.com/gorilla/mux"
	"github.com/pquerna/otp/totp"
)

func InboxGet(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	var mail_id int
	var totp_token string
	var err error
	if mail_id, err = strconv.Atoi(vars["mail_id"]); err != nil {
		panic(err)
	}
	if totp_token = vars["totp_token"]; err != nil {
		panic(err)
	}

	if totp.Validate(totp_token, RepoGetUser(mail_id)) {

		inbox := RepoFindInbox(mail_id)

		if len(inbox) > 0 {
			w.Header().Set("Content-Type", "application/json; charset=UTF-8")
			w.WriteHeader(http.StatusOK)
			if err := json.NewEncoder(w).Encode(inbox); err != nil {
				panic(err)
			}
		} else {
			w.Header().Set("Content-Type", "application/json; charset=UTF-8")
			w.WriteHeader(http.StatusNotFound)
			if err := json.NewEncoder(w).Encode(jsonErr{Code: http.StatusNotFound, Text: "No Emails"}); err != nil {
				panic(err)
			}
		}
	} else { // 403 bad token
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
		w.WriteHeader(http.StatusForbidden)
		if err := json.NewEncoder(w).Encode(jsonErr{Code: http.StatusForbidden, Text: "Bad TOTP Token"}); err != nil {
			panic(err)
		}
	}
}

func GenNewSecret() string {
	key, err := totp.Generate(totp.GenerateOpts{
		Issuer:      "SecureMail",
		AccountName: ".",
	})
	if err != nil {
		panic(err)
	}
	return key.Secret()
}

func RegisterGet(w http.ResponseWriter, r *http.Request) {
	secret := GenNewSecret()

	w.Header().Set("Content-Type", "application/json; charset=UTF-8")
	w.WriteHeader(http.StatusOK)
	if err := json.NewEncoder(w).Encode(RepoRegister(secret)); err != nil {
		panic(err)
	}
}

func MailPost(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	var mail Mail
	var sender_id int
	var totp_token string
	var recipient_id int
	var err error

	if sender_id, err = strconv.Atoi(vars["sender_id"]); err != nil {
		panic(err)
	}

	if totp_token = vars["totp_token"]; err != nil {
		panic(err)
	}

	if totp.Validate(totp_token, RepoGetUser(sender_id)) {
		if recipient_id, err = strconv.Atoi(vars["recipient_id"]); err != nil {
			panic(err)
		}

		body, err := ioutil.ReadAll(io.LimitReader(r.Body, 1048576))
		if err != nil {
			panic(err)
		}
		if err := r.Body.Close(); err != nil {
			panic(err)
		}
		if err := json.Unmarshal(body, &mail); err != nil {
			w.Header().Set("Content-Type", "application/json; charset=UTF-8")
			w.WriteHeader(422) // unprocessable entity
			if err := json.NewEncoder(w).Encode(err); err != nil {
				panic(err)
			}
		}

		mail.Header.Sender = sender_id
		mail.Header.Recipient = recipient_id
		mail.Header.Timestamp = time.Now()

		m := RepoCreateMail(mail)
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
		w.WriteHeader(http.StatusCreated)
		if err := json.NewEncoder(w).Encode(m); err != nil {
			panic(err)
		}
	} else {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
		w.WriteHeader(http.StatusForbidden)
		if err := json.NewEncoder(w).Encode(jsonErr{Code: http.StatusForbidden, Text: "Bad TOTP Token"}); err != nil {
			panic(err)
		}
	}
}
