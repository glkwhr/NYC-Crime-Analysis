var dlabels = []
var s1 = [];
var s2 = [];
var s3 = [];


$(document).ready(function() {
	$.ajax({
		type: "GET",
		url: "kycdTime.csv",
		dataType: "text",
		success: function(data) {processCSV(data);}
	});
});

function processCSV(data){
	for(i = 0; i <=23; i++){
		dlabels.push(i.toString()+":00");
	}
	for(i = 0; i <=23; i++){
		s1.push(0);
	}
	for(i = 0; i <=23; i++){
		s2.push(0);
	}
	for(i = 0; i <=23; i++){
		s3.push(0);
	}

	lines = data.split(/\n|\r\n/);
	for(i = 0;i < lines.length; i++){
		datas = lines[i].split(",");
		code = parseInt(datas[0]);
		time = parseInt(datas[1]);
		number = parseInt(datas[2]);
		if(code < 300){
			s1[time] += number;
		}
		else if(code < 500){
			s2[time] += number;
		}
		else{
			s3[time] += number;
		}
	}
	drawGraph();
}
function drawGraph(){
	var data = {
		labels: dlabels,
		series: [s1,s2,s3]
	};
	var options = {
		stackBars: true,
		width: 1000,
		height: 600,
		axisX: {
			offset: 30
		},
		axisY: {
			offset: 80,
			scaleMinSpace: 15
		}
	}
	new Chartist.Bar('.ct-chart_x', data, options).on('draw', function(data) {
  		if(data.type === 'bar') {
    		data.element.attr({
      			style: 'stroke-width: 30px'
    		});
  		}
	});
}