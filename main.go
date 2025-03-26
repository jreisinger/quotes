package main

import (
	"flag"
	"fmt"
	"math/rand"
	"strings"

	_ "embed"
)

//go:embed quotes.txt
var quotes string

func main() {
	v := flag.Bool("v", false, "be verbose")
	r := flag.Bool("r", false, "random quote")
	flag.Parse()

	lines := strings.Split(quotes, "\n\n")
	nLines := len(lines)

	if *r {
		randIdx := rand.Intn(nLines)
		randQuote := lines[randIdx]
		if *v {
			fmt.Printf("[%d/%d] ", randIdx+1, nLines)
		}
		fmt.Println(randQuote)
	} else {
		for i, line := range lines {
			if *v {
				fmt.Printf("[%d/%d] ", i+1, nLines)
			}
			if i == len(lines)-1 { // last line
				fmt.Print(line)
			} else {
				fmt.Println(line)
			}
		}
	}
}
