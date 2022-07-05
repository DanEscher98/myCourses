package main

import (
	"fmt"
	"log"
)

type Shark struct {
	Name string
}

func (s *Shark) SayHello() {
	fmt.Println("Hi! My name is", s.Name)
}

func divide(a, b int) int {
	return a / b
}

func divideByZero() {
	defer func() {
		if err := recover(); err != nil {
			log.Println("panic ocurred: ", err)
		}
	}()
	fmt.Println(divide(1, 0))
}

func main() {
	s := &Shark{"Sammy"}
	// s = nil
	s.SayHello()

	divideByZero()
	fmt.Println("we survived dividing by zero!")
}
