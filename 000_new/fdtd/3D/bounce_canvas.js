var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
c.addEventListener('click', on_canvas_click, false);

width = c.width;
height = c.height;

var n = 20;
var x = new Array(n);
var y = new Array(n);
var vy = new Array(n);
var vx = new Array(n);
var g = 0.05;
var cor = 0.7;
var fr = 0.95;
var r = 5;

for (i=0; i < n; ++i) {
	x[i] = 300;
	y[i] = 100;
	vx[i] = 2*(Math.random()-.5);
	vy[i] = 2*(Math.random()-.5);
}

function updateY(i) {
	if ((y[i]+r) < height) {
		// y = height;
		vy[i] += g;
	} else {
		vy[i] = -vy[i]*cor;
		vx[i] *= fr;
	}
	y[i] += vy[i];
	if ((y[i]+r) > height) {
		y[i] = height-r;
	}
}

function updateX(i) {
	if ((x[i]+r) >= width || (x[i]-r) <= 0) {
		vx[i] = -vx[i]*cor;
	}
	x[i] += vx[i];
	if ((x[i]+r) > width) {
		x[i] = width-r;
	} else if ((x[i]-r) < 0) {
		x[i] = r;
	}
}

function circle(x,y,r) {
   ctx.beginPath();
   ctx.arc(x, y, r, 0, Math.PI*2, true);
   ctx.fill();
   }

function text(s) {
   ctx.fillStyle = "#ff0000";
   ctx.font = "30px sans-serif";
   ctx.textBaseline = "bottom";
   ctx.fillText(s,0,height);
   }

function animate() {
	ctx.clearRect(0, 0, width, height);
   	ctx.fillStyle = "#000000";
	for (i = 0; i < n; ++i) {
		updateY(i);
		updateX(i);
		circle(x[i],y[i],r);
	}

}

text("Click me!");

function on_canvas_click(ev) {
	// animate();
	window.setInterval("animate()",0);
}