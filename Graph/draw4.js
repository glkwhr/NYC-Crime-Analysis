var dlabels = []
var s1 = [];


$(document).ready(function() {
	$.ajax({
		type: "GET",
		url: "hour.csv",
		dataType: "text",
		success: function(data) {processCSV(data);}
	});
});

function processCSV(data){
	lines = data.split(/\n|\r\n/);
	for(i = 0;i < lines.length; i++){
		datas = lines[i].split(",");
		dlabels.push(datas[0]);
		s1.push(parseInt(datas[1]));
	}
	drawGraph();
}
function drawGraph(){
	var data = {
		labels: dlabels,
		series: [s1]
	};
	var options = {
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
	new Chartist.Line('.ct-chart_x', data, options);
}