package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	introduction()
}

func introduction() string {
	fmt.Println("Welcome to Manchester Metropolitan University")
	fmt.Println("The university has been taken over by AI robots. Thanks to the A.I students >:O")
	fmt.Println("What is your name")

	for {
		getName := func() string {
			scanner := bufio.NewScanner(os.Stdin)
			scanner.Scan()

			return scanner.Text()
		}
		name := getName()
		if strings.TrimLeft(name, "") != "" {
			fmt.Printf("Hello %s\n", name)
			return name
		}
		fmt.Println("Please enter a name")
	}
}
