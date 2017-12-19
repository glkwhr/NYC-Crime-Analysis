var dlabels = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
var s1 = [];
var s2 = [];
var s3 = [];

$(document).ready(function() {
	$.ajax({
		type: "GET",
		url: "boroCrimeLevel.csv",
		dataType: "text",
		success: function(data) {processCSV(data);}
	});
});

function processCSV(data){
	lines = data.split(/\n|\r\n/);
	for(i = 0;i < lines.length; i++){
		datas = lines[i].split("*");
		if(i%3 == 1){
			s2.push(parseInt(datas[2]));
		}
		if(i%3 == 2){
			s3.push(parseInt(datas[2]));
		}
		if(i%3 == 0){
			s1.push(parseInt(datas[2]));
		}
	}
	drawGraph();
}
function drawGraph(){
	var data = {
		labels: dlabels,
		series:[s1, s2, s3]
	}
	var options = {
		seriesBarDistance: 30,
		width: 1000,
		height: 600,
		axisX: {
			offset: 30
		},
		axisY: {
			offset: 80,
			labelInterpolationFnc: function(value) {
				return value;
			},
			scaleMinSpace: 15
		}
	}
	new Chartist.Bar('.ct-chart_x', data, options).on('draw', function(data) {
  			if(data.type === 'bar') {
    			data.element.attr({
      			style: 'stroke-width: 20px'
    		});
  		}
	});
}