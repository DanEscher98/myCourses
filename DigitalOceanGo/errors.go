package main

import (
	"errors"
	"fmt"
	"net/http"
	"os"
	"strings"
	"time"
)

func capitalize(name string) (string, int, error) {
	handle := func(err error) (string, int, error) {
		return "", 0, err
	} // anonymous function to simplify the error return

	if name == "" {
		return handle(errors.New("no name provided"))
	}
	return strings.ToTitle(name), len(name), nil
}

// CUSTOM ERRORS

type MyError struct{}

func (m *MyError) Error() string {
	return "boom"
}

func sayHello() (string, error) {
	return "", &MyError{}
}

// Type assertions

type RequestError struct {
	StatusCode int
	Err        error
}

func (r *RequestError) Error() string {
	return r.Err.Error()
}

func (r *RequestError) Temporary() bool {
	return r.StatusCode == http.StatusServiceUnavailable
}

func doRequest() error {
	return &RequestError{
		StatusCode: 503,
		Err:        errors.New("unavailable"),
	}
}

// Wrapping Erros

type WrappedError struct {
	Context string
	Err     error
}

func (w *WrappedError) Error() string {
	return fmt.Sprintf("%s: %v", w.Context, w.Err)
}

func Wrap(err error, info string) *WrappedError {
	return &WrappedError{
		Context: info,
		Err:     err,
	}
}

func main_d() {
	err_1 := errors.New("prianhana")
	err_2 := fmt.Errorf("error occurred: %v", time.Now())
	fmt.Println("Simmon says: ", err_1)
	fmt.Println("An error: ", err_2)

	name, size, err_c := capitalize("daniel")
	if err_c != nil {
		fmt.Println("Could not capitalize: ", err_c)
		return
	}
	fmt.Printf("Capitalized name: %s, len: %d", name, size)

	s, err := sayHello()
	if err != nil {
		fmt.Println("unexpected error: ", err)
		os.Exit(1)
	}
	fmt.Println("The string: ", s)

	err_r := doRequest()
	if err_r != nil {
		fmt.Println(err)
		re, ok := err.(*RequestError)
		if ok {
			if re.Temporary() {
				fmt.Println("This request can be tried again")
			} else {
				fmt.Println("This request cannot be tried again")
			}
		}
		os.Exit(1)
	}
	fmt.Println("success!")

	err_w := errors.New("boom!")
	err = Wrap(err, "main")
	fmt.Println(err_w)
}
