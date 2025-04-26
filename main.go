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
		printQuote(q)
	}
}

func (qs Quotes) printRandom() {
	i := rand.Intn(len(qs.quotes))
	if qs.withPrefix {
		printPrefix(i, len(qs.quotes))
	}
	printQuote(qs.quotes[i])
}

func printPrefix(i, total int) {
	cyan := "\033[36m" // Color for the prefix
	reset := "\033[0m" // Reset color to default
	fmt.Printf("%s%d%s/%s%d%s ", cyan, i+1, reset, cyan, total, reset)
}

func printQuote(quote string) {
	blue := "\033[94m"   // Color for the author
	yellow := "\033[33m" // Color for the source (URL)
	reset := "\033[0m"   // Reset color to default

	parts := strings.SplitN(quote, " --", 2)
	if len(parts) == 2 {
		authorParts := strings.SplitN(parts[1], "(", 2)
		if len(authorParts) == 2 {
			// Print quote, author, and source separately
			fmt.Printf("%s --%s%s %s(%s%s%s)\n",
				parts[0], blue, strings.TrimRight(authorParts[0], ` `), reset, yellow, strings.TrimSuffix(authorParts[1], ")"), reset)
		} else {
			// Print quote and author only
			fmt.Printf("%s --%s%s%s\n",
				parts[0], blue, parts[1], reset)
		}
	} else {
		// Print quote only
		fmt.Println(quote)
	}
}
