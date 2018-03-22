javascript:
var cTime = document.getElementsByClassName("subinterdiv");
var cSubmit = document.getElementsByClassName("submit-submit");
var oBody = document.getElementsByTagName("body")[0];

var oSign = document.createElement('div');
oSign.innerHTML = "<h1> waiting to submit... </h1>";
oSign.style.position = "fixed";
oSign.style.top = "0";
oSign.style.left = "0";
oBody.appendChild(oSign);

if(cTime.length)
{
	var oTime = cTime[0];
	var index = setInterval(function(){
		if(oTime.getElementsByClassName("gcolor").length)
		{
			cSubmit[0].click();
			clearInterval(index);
		}
	}, 1000);
}
else
{
	cSubmit[0].click();
}
