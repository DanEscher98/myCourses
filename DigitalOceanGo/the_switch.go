package main

import (
	"fmt"
	"math/rand"
)

func main_c() {
	target := rand.Intn(100)
	for {
		var guess int
		fmt.Print("Enter a guess: ")
		_, err := fmt.Scanf("%d", &guess)
		if err != nil {
			fmt.Println("Invalid guess: ", err)
			continue
		}

		switch {
		case guess > target:
			fmt.Println("Too high!")
		case guess < target:
			fmt.Println("Too low!")
		default:
			fmt.Println("You win!")
			return
		}
	}
}
