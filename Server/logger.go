package main

import (
	"log"
	"net/http"
	"strings"
	"time"
)

func Logger(inner http.Handler, name string) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()

		inner.ServeHTTP(w, r)

		log.Printf(
			"%s%s%s\t%s",
			leftjust(r.Method, 8),
			leftjust(r.RequestURI, 31),
			leftjust(name, 16),
			time.Since(start),
		)
	})
}

func leftjust(s string, n int) string {
	return s + strings.Repeat(" ", n-len(s))
}
