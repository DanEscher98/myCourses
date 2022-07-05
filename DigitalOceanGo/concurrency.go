package main

import (
	"fmt"
	"sync"
)

func generateNumbers(total int, ch chan<- int, wg *sync.WaitGroup) {
	for idx := 1; idx <= total; idx++ {
		fmt.Printf("sending '%d' to channel\n", idx)
		ch <- idx
	}
}

func printNumbers(idx int, ch <-chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for num := range ch {
		fmt.Printf("#%d: read '%d' from channel\n", idx, num)
	}
}

func main_b() {
	var wg sync.WaitGroup
	numberChan := make(chan int)

	for idx := 1; idx <= 3; idx++ {
		wg.Add(1)
		go printNumbers(idx, numberChan, &wg)
	}
	generateNumbers(10, numberChan, &wg)
	close(numberChan) // avoids a deadlock

	fmt.Println("Waiting for gorutines to finish...")
	wg.Wait()
	fmt.Println("Done!")
}
