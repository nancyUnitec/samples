//require contents from mac in company.

//log

//format

//marshal and unmarshal

//struct to json
func testMarshal(){
    fmt.Printf ( "mmmmmmmmmmmmmmmmmmmarshal \n" ) 
    type ColorGroup struct { 
        ID     int 
        Name   string 
        Colors [ ] string 
    } 
    group := ColorGroup { 
        ID :     1 , 
        Name :   "Reds" , 
        Colors : [ ] string { "Crimson" , "Red" , "Ruby" , "Maroon" } , 
    } 
    b , err := json. Marshal ( group ) 
    if err != nil { 
        fmt. Println ( "error:" , err ) 
    } 
    os. Stdout . Write ( b ) 
    //output is a json format: {"ID":1,"Name":"Reds","Colors":["Crimson","Red","Ruby","Maroon"]}
}

//json to struct
func testUnMarshal(){
    fmt.Printf ( "\n uuuuuuuuuuuuunmarshal \n" ) 
    var jsonBlob = [ ] byte ( ` [ 
        { "Name" : "Platypus" , "Order" : "Monotremata" } , 
        { "Name" : "Quoll" ,     "Order" : "Dasyuromorphia" } 
    ] ` ) 
    type Animal struct { 
        Name  string 
        Order string 
    } 
    var animals [ ] Animal 
    err := json. Unmarshal ( jsonBlob , & animals ) 
    if err != nil { 
        fmt. Println ( "error:" , err ) 
    } 
    fmt.Printf ( "%+v" , animals ) 
    //output: [{Name:Platypus Order:Monotremata} {Name:Quoll Order:Dasyuromorphia}]
}