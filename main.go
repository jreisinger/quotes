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
	p := flag.Bool("p", false, "add prefix")
	r := flag.Bool("r", false, "random quote")
	flag.Parse()

	quotes := newQuotes(quotes, *p)
	if *r {
		quotes.printRandom()
	} else {
		quotes.printAll()
	}
}

type Quotes struct {
	quotes     []string
	withPrefix bool
}

func newQuotes(quotes string, withPrefix bool) Quotes {
	var qs []string
	for _, q := range strings.Split(quotes, "\n\n") {
		q = strings.TrimSpace(q)
		qs = append(qs, q)
	}
	return Quotes{
		quotes:     qs,
		withPrefix: withPrefix,
	}
}

func (qs Quotes) printAll() {
	for i, q := range qs.quotes {
		if qs.withPrefix {
			printPrefix(i, len(qs.quotes))
		}
		fmt.Println(q)
	}
}

func (qs Quotes) printRandom() {
	i := rand.Intn(len(qs.quotes))
	if qs.withPrefix {
		printPrefix(i, len(qs.quotes))
	}
	fmt.Println(qs.quotes[i])
}

func printPrefix(i, total int) {
	fmt.Printf("[%d/%d] ", i+1, total)
}
