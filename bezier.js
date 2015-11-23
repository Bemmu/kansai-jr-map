function drawStuff() {
	context.clearRect(0, 0, canvas.width, canvas.height);

	context.beginPath();
	context.moveTo(188, 130);
	context.bezierCurveTo(140, 10, 388, 10, 388, 170);
	context.lineWidth = 10;
	context.strokeStyle = 'black';
	context.stroke();

    window.requestAnimationFrame(drawStuff);
}
