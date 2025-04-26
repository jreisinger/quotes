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
	count      int
	withPrefix bool
}

func newQuotes(quotes string, withPrefix bool) Quotes {
	ss := strings.Split(quotes, "\n\n")
	return Quotes{
		quotes:     ss,
		count:      len(ss),
		withPrefix: withPrefix,
	}
}

func (qs Quotes) printAll() {
	for i, q := range qs.quotes {
		if qs.withPrefix {
			printPrefix(i, qs.count)
		}
		if i == qs.count-1 { // last line
			fmt.Print(q)
		} else {
			fmt.Println(q)
		}
	}
}

func (qs Quotes) printRandom() {
	i := rand.Intn(qs.count)
	if qs.withPrefix {
		printPrefix(i, qs.count)
	}
	fmt.Println(qs.quotes[i])
}

func printPrefix(i, total int) {
	fmt.Printf("[%d/%d] ", i+1, total)
}
