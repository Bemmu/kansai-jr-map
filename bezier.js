// Playing with cubic bezier curves
function curveXY(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y, t) {
	var x = Math.pow(1-t, 3)*p0x + 3*Math.pow(1-t, 2)*t*p1x + 3*(1-t)*Math.pow(t, 2)*p2x + Math.pow(t, 3)*p3x;
	var y = Math.pow(1-t, 3)*p0y + 3*Math.pow(1-t, 2)*t*p1y + 3*(1-t)*Math.pow(t, 2)*p2y + Math.pow(t, 3)*p3y;
	return {
		'x' : x,
		'y' : y
	}
}

var start = Date.now();

function drawStuff() {
	context.clearRect(0, 0, canvas.width, canvas.height);

	var p0x = 188; var p0y = 130;
	var p1x = 140; var p1y = 10;
	var p2x = 388; var p2y = 10;
	var p3x = 888; var p3y = 170;

	context.beginPath();
	context.moveTo(p0x, p0y);
	context.bezierCurveTo(p1x, p1y, p2x, p2y, p3x, p3y);
	context.lineWidth = 10;
	context.strokeStyle = 'black';
	context.stroke();

//	for (var t = 0.0; t < 1.0; t += 0.01) {
	var t = (Date.now()-start)%1000/1000.;
	var p = curveXY(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y, t);
	context.fillStyle = 'white';
	context.fillRect(-3 + p.x, -3 + p.y, 7, 7);
	context.fillStyle = 'black';
	context.fillRect(-2 + p.x, -2 + p.y, 5, 5);
	// }

    window.requestAnimationFrame(drawStuff);
}
