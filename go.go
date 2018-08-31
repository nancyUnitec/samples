import (
	"encoding/json"
	"fmt"
	"os"
)

//require contents from mac in company.

//log

//format

//build go project fail:
//if the error is funcxxx not defined in packxxx, for example, can't find round() in math pkg.
//if packxxx is from the base go library, upgrade the go version, using brew
//or else, remove the pkg,vendor,gopkg.lock,gopkg.toml and then dep init, dep ensure...


//marshal and unmarshal

//struct to json
func testMarshal() {
	fmt.Printf("mmmmmmmmmmmmmmmmmmmarshal \n")
	type ColorGroup struct {
		ID     int
		Name   string
		Colors []string
	}
	group := ColorGroup{
		ID:     1,
		Name:   "Reds",
		Colors: []string{"Crimson", "Red", "Ruby", "Maroon"},
	}
	b, err := json.Marshal(group)
	if err != nil {
		fmt.Println("error:", err)
	}
	os.Stdout.Write(b)
	//output is a json format: {"ID":1,"Name":"Reds","Colors":["Crimson","Red","Ruby","Maroon"]}
}

//json to struct
func testUnMarshal() {
	fmt.Printf("\n uuuuuuuuuuuuunmarshal \n")
	var jsonBlob = []byte(` [ 
        { "Name" : "Platypus" , "Order" : "Monotremata" } , 
        { "Name" : "Quoll" ,     "Order" : "Dasyuromorphia" } 
    ] `)
	type Animal struct {
		Name  string
		Order string
	}
	var animals []Animal
	err := json.Unmarshal(jsonBlob, &animals)
	if err != nil {
		fmt.Println("error:", err)
	}
	fmt.Printf("%+v", animals)
	//output: [{Name:Platypus Order:Monotremata} {Name:Quoll Order:Dasyuromorphia}]
}

//pubsub messages
//not to publist the message, use
msg.Ack()

//resend the msg immediately
msg.Nack()

//resend the msg every 60 secs
do nothing, return directly 

//correct method of tracing code:
//write a number to represent the level order, then the call stack can be seen
ReadDistributionsOfRateIDGroupBySaleBlock
0 GetAllDataByRateID
1 goRoutineSearchFailureDistributionOfRateGroupBySaleBlock
2 GenerateSQLForFailureDistributionOfRateGroupBySaleBlock
2 failureDistribution, err := ReadMapOfFailureDistribution(ctx, spannerClient, sqlForSummaries, paramsForSummaries)

0 GetAllDataByRateID
1 goRoutineSearchFailureDistributionOfRateGroupBySaleBlock
2 GenerateSQLForFailureDistributionOfRateGroupBySaleBlock
3 failureDistribution, err := ReadMapOfFailureDistribution(ctx, spannerClient, sqlForSummaries, paramsForSummaries)
