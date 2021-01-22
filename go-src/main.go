package main

import (
	"fmt"
	"io/ioutil"
	"proto-demo/product_proto"
	"github.com/golang/protobuf/proto"
)

func main(){
	fmt.Println("Hello World")
	data, _:= ioutil.ReadFile("product_binary")
	fmt.Println(data)
	p := product_proto.ProductResponse{}
	fmt.Println(p)
	proto.Unmarshal(data, &p)
	//fmt.Println(p.Tags[0].Title)
	for _, tag := range p.Tags{
		fmt.Println(tag.Title)
	}

}
