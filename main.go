package main

import (
	"fmt"
	"math/rand"
	"strings"

	_ "embed"
)

//go:embed quotes.txt
var quotes string

func main() {
	lines := strings.Split(quotes, "\n\n")
	randQuote := lines[rand.Intn(len(lines))]
	fmt.Println(randQuote)
}
