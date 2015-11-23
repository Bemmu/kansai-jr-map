var canvas = document.getElementsByClassName('canvas')[0];
console.log(canvas);

var context = canvas.getContext('2d');

// resize the canvas to fill browser window dynamically
window.addEventListener('resize', resizeCanvas, false);

function resizeCanvas() {
	canvas.width = window.innerWidth;
	h = canvas.height = window.innerHeight;
	console.log("resized " + window.innerWidth);
}
resizeCanvas();

// Find vendor-specific way to do smooth animation
if (!window.requestAnimationFrame && window.webkitRequestAnimationFrame) {
	window.requestAnimationFrame = window.webkitRequestAnimationFrame;
}
if (!window.requestAnimationFrame && window.mozRequestAnimationFrame) {
	window.requestAnimationFrame = window.mozRequestAnimationFrame;
}
drawStuff();

