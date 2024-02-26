package main

import (
	"fmt"
	"log"

	"github.com/jonas-p/go-shp"
)

type Sheet struct {
	Columns []Column
}

type Column struct {
	Name   string
	Values []string
}

func read(file string) ([]Column, error) {
	var cols []Column
	shape, err := shp.Open(file)
	if err != nil {
		return cols, err
	}
	defer shape.Close()
	fields := shape.Fields()
	for _, value := range fields {
		vals := []string{"a", "b", "c"}
		new_val := value.String()
		new_col := Column{Name: new_val, Values: vals}
		cols = append(cols, new_col)
	}
	return cols, err
}

func main() {
	file := "*"
	x, err := read(file)
	if err != nil {
		log.Fatal(err)
	}
	for _, v := range x {
		fmt.Println(v.Name)
	}

}
