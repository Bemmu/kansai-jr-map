// Playing with cubic bezier curves
function curveXY(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y, t) {
	var x = Math.pow(1-t, 3)*p0x + 3*Math.pow(1-t, 2)*t*p1x + 3*(1-t)*Math.pow(t, 2)*p2x + Math.pow(t, 3)*p3x;
	var y = Math.pow(1-t, 3)*p0y + 3*Math.pow(1-t, 2)*t*p1y + 3*(1-t)*Math.pow(t, 2)*p2y + Math.pow(t, 3)*p3y;
	return {
		'x' : x,
		'y' : y
	}
}

// A bit of magic that gives the proper amount to increment t by to make 
// movement along a cubic bezier curve have constant acceleration.
// http://gamedev.stackexchange.com/questions/27056/how-to-achieve-uniform-speed-of-movement-on-a-bezier-curve
function curveIncrement(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y, t) {
	var v1x = -3*p0x +  9*p1x  - 9*p2x + 3*p3x;
	var v1y = -3*p0y +  9*p1y  - 9*p2y + 3*p3y;
	var v2x =  6*p0x - 12*p1x  + 6*p2x;
	var v2y =  6*p0y - 12*p1y  + 6*p2y;
	var v3x = -3*p0x +  3*p1x;
	var v3y = -3*p0y +  3*p1y;

	var x = t*t*v1x + t*v2x + v3x;
	var y = t*t*v1y + t*v2y + v3y;
	var length = Math.sqrt(x*x + y*y);
	return length;
}

var start = Date.now();
var prev = Date.now();
var t = 0;

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
//	var t = (Date.now()-start)%1000/1000.;
//	t += (Date.now() - prev)*0.001;

	var elapsed = (Date.now() - prev)*0.001;
	t = t + 2./curveIncrement(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y, t);

//	x*y*y = z

	if (t > 1) t = 0;
	prev = Date.now();

	var p = curveXY(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y, t);
	context.fillStyle = 'white';
	context.fillRect(-3 + p.x, -3 + p.y, 7, 7);
	context.fillStyle = 'black';
	context.fillRect(-2 + p.x, -2 + p.y, 5, 5);
	// }

    window.requestAnimationFrame(drawStuff);
}
