package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scan(&s)
	arr := strings.Split(s, "")

	count := 0

	for _, v := range arr {
		if v == "1" {
			count ++
		}
	}

	fmt.Println(count)
}