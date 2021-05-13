package main

import (
    "log"
    "net/http"
    "strconv"
    "encoding/json"
    "github.com/gorilla/mux"
)

type Fibonacci struct {
	Value int `json:"value,omitempty"`
}

type Result struct {
	Data Fibonacci `json:"data"`
}

func FibonacciSequence(w http.ResponseWriter, r *http.Request){
    params := mux.Vars(r)
    order, err := strconv.Atoi(params["order"])
    _ = err
    var f []int
    f = append(f, 0)
    f = append(f, 1)
    for i := 2; i <= order; i++ {
        f = append(f, f[i - 1] + f[i - 2]);
    }
    fibonacci := Fibonacci{Value: f[order]}
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(Result{Data: fibonacci})
}

func main() {
    router := mux.NewRouter().StrictSlash(true)
    router.HandleFunc("/fibonacci/v1/sequence/{order:[0-9]+}", FibonacciSequence).Methods("GET")
    log.Println("App running -> http://localhost:3000")
    log.Fatal(http.ListenAndServe(":3000", router))
}