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
	