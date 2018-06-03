//arrow function & the typical usage of map()
var materials = [
  'Hydrogen',
  'Helium',
  'Lithium',
  'Beryllium'
];

materials.map(function(material) { 
  return material.length; 
}); // [8, 6, 7, 9]

materials.map((material) => {
  return material.length;
}); // [8, 6, 7, 9]

//shorter
materials.map(material => material.length); // [8, 6, 7, 9]

//convert number to string:
key = "expected_SM" + demo_months[j].toString()

//create an array and mutate its elements
var yxArr = new Array(len)
for (let i = 0; i < len; i++) {

  yxArr[i] = {}
  yxArr[i].xx = old_xxxx[i].xxx
  yxArr[i].P = "P" + i.toString()
  if (new_data) {
    if (new_data.length > 0)
      yxArr[i].new_xx = new_data[i].xxx
  }
}

//In an array, get the index of a certain element & output the greatest integer less than or equal to
sm_list.indexOf(id)
Math.floor(num)
Math.floor(sm_list.indexOf(id)/3)

alert(Math.ceil(25.1)); //the smallest integer greater than or equal
alert(Math.round(25.9)); //si she wu ru

//the use of eval()
var evalString="testEval()"

function testEval(){
	alert("testEval!");
}

function testjs()
{
  eval(evalString); //will call testEval. eval is  used to create js dynamic code 
  //like function pointer to some extent
}

//document.getElementById("").attr
function forLoop(){
  for (var loop = 1; loop < 10; loop++)
	{
		// eval('document.getElementById("div"+loop).innerHTML="123"');
		document.getElementById("div"+loop).innerHTML="123"; //will show "123" in div1,div2 and div3
	}
}

this.props.condition_items.forEach((item, index) => console.log("condition item. item: ", item))
//condition item. item:  {period_months_index: "", period_months: 0, price_to_index: "", price_to: 0, class_id: "", …}
//condition item. item:  {period_months_index: "", period_months: 0, price_to_index: "", price_to: 0, class_id: "190", …}

this.props.condition_items.forEach((item, index) => console.log("condition item. index: ", index))
//condition item. index:  0
//condition item. index:  1

//get key and value from object
compare = {SM2: 35.76, expected_SM2: 105.11, new_SM2: 35.76, SM4: 0, expected_SM4: 108.17}
for (var pl in compare) {    //pl is key
  console.log("pl", pl);   //SM2 / expected_SM2
  console.log("value[pl]", compare[pl])   //35.76 / 105.11
  sm_list.push(pl)  //sm_list: SM2, expected_SM2, new_SM2....
}


//...
function testDotDotDot()
{
	const a = {
        a: 1,
        b: 2,
        c: 3
    };
    const b = {
    ...a,
    d: [],
    b: 5  //this will update the b value in a{}
    }
    console.log(b);
    //output:{a: 1, b: 5, c: 3, d: Array(0)}
}

//testslice
function testjs()
{
	alert("test!");
  // rocker.invoke()
  
  var arr = new Array(6)
  arr[0] = "George"
  arr[1] = "John"
  arr[2] = "Thomas"
  arr[3] = "James"
  arr[4] = "Adrew"
  arr[5] = "Martin"

  document.write(arr + "<br />")   //output George,John,Thomas,James,Adrew,Martin
  document.write(arr.slice(2,4) + "<br />") //output arr[2],arr[3] Thomas,James
  document.write(arr.slice(2) + "<br />")
  document.write(arr.slice() + "<br />")
}

//react: semantic-ui
//import { Dropdown, Form, Input, Label, Checkbox } from 'semantic-ui-react'

//show by conditions  &&  map an array to widgets groups
//n elemets in the array will generate n groups of widgets
{this.props.condition_items.length > 0 && this.props.condition_items.map((item, index) => (
<Form key={index}>
              <Form.Group>
                <ConditionRow index={index} condition_item={item} class_options={this.props.class_options} brand_options={this.props.brand_options} period_months_options={period_months_options} price_to_options={price_to_options} month_option={options}  dispatch={this.props.dispatch} />
                <Form.Field>
                <Button size='small' color={item.is_saved ? 'blue' : 'red'} loading={item.save_loading} onClick={() => this.saveConditionRow(index, item)}>
                    {item.is_saved && <Icon name='checkmark' />}
                    {item.is_saved ? 'Saved' : 'Unsaved'}
                  </Button>
                </Form.Field>
              </Form.Group>
            </Form>
))}


Promise.resolve("foo")
  // 1. 接收 "foo" 并与 "bar" 拼接，并将其结果做为下一个resolve返回。
  .then(
  function(string) {  
    return new Promise(function(resolve, reject) {
      setTimeout(function() {string += 'bar';resolve(string);}, 1);
    }
	
	);
  })
  // 2. 接收 "foobar", 放入一个异步函数中处理该字符串
  // 并将其打印到控制台中, 但是不将处理后的字符串返回到下一个。
  .then(function(string) {
    setTimeout(function() {
      string += 'baz';
      console.log(string);
    }, 1)
    return string;
  })
  // 3. 打印本节中代码将如何运行的帮助消息，
  // 字符串实际上是由上一个回调函数之前的那块异步代码处理的。
  .then(function(string) {
    console.log("Last Then:  oops... didn't bother to instantiate and return " +
                "a promise in the prior then so the sequence may be a bit " +
                "surprising");

    // 注意 `string` 这时不会存在 'baz'。
    // 因为这是发生在我们通过setTimeout模拟的异步函数中。
    console.log(string);
});
	
doSomething(
   function(result) {
   doSomethingElse(
    result, 
  
  function(newResult) {
    doThirdThing(
	newResult, 
	function(finalResult) {
      console.log('Got the final result: ' + finalResult);
    }, 
	failureCallback
	);
  }, 
  
  failureCallback);
}, 

failureCallback

);

