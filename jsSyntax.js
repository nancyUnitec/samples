//arrow function

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

