package main

import (
	"log"
	"net/http"

	"github.com/gorilla/handlers"
)

func main() {

	router := NewRouter()

	originsOk := handlers.AllowedOrigins([]string{"*"})

	log.Fatal(http.ListenAndServe(":8080", handlers.CORS(originsOk)(router)))
}
