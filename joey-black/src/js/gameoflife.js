var canvas;
var context;

var canvasw=1000;
var canvash=600;

var cellw = 6;
var cellh = 6;

var worldw = (canvasw/cellw) | 0;
var worldh = (canvash/cellh) | 0;

var alive;



Array.prototype.clone = function()
{
	var arr = this.slice(0);
	for(var i=0; i<this.length; i++)
	{
		if (this[i].clone)
		{
			arr[i] = this[i].clone();
		}
	}
	return arr;
};


function neighborCount(x,y)
{
	var neighbors = 0;
	if (y>0)
	{
		if (alive[y-1][x]) neighbors++;
	}
	if (y<worldh-1)
	{
		if (alive[y+1][x]) neighbors++;
	}
	
	if (x>0)
	{
		if (alive[y][x-1]) neighbors++;
		if (y>0)
		{
			if (alive[y-1][x-1]) neighbors++;
		}
		if (y<worldh-1)
		{
			if (alive[y+1][x-1]) neighbors++;
		}
	}
	
	if (x<worldw-1)
	{
		if (alive[y][x+1]) neighbors++;
		if (y>0)
		{
			if (alive[y-1][x+1]) neighbors++;
		}
		if (y<worldh-1)
		{
			if (alive[y+1][x+1]) neighbors++;
		}
	}
	return neighbors;
}


// Update cells according to game of life rules
function updateLife()
{
	var temp = alive.clone();
	allcells(function (x,y) {
		var neighbors = neighborCount(x,y);
		if (neighbors==3) temp[y][x] = true;
		else if (neighbors!=2) temp[y][x] = false;
	});
	alive = temp;
}


// drawing, animation and interface stuff


function Point(x, y) {
    this.x=x;
    this.y=y;
}

function Cell(x, y)
{
    this.x=x|0;
    this.y=y|0;
}

function getCursorPosition(e) {
    /* returns Point with x and y properties */
    var x;
    var y;
    if (e.pageX || e.pageY) {
		x=e.pageX;
		y=e.pageY;
    }
    else {
		x=e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
		y=e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
    }
    x-=canvas.offsetLeft;
    y-=canvas.offsetTop;
    x=Math.min(x, canvasw);
    y=Math.min(y, canvash);
    var point = new Point(x, y);
    return point;
}

function mouseEvent(e) {
    var point=getCursorPosition(e);
    var newc = new Cell(point.x/cellw, point.y/cellh);
    
    alive[newc.y][newc.x] = !alive[newc.y][newc.x];
    
    drawWorld();
}


function drawCell(x,y)
{
	context.translate(0, 0);
	context.fillStyle    = '#444444';
	context.fillRect(x*cellw, y*cellh, cellw, cellh);
}

function allcells(fun)
{
	for ( var y = 0; y < worldh; y++) 
	{
		for ( var x = 0; x < worldw; x++) 
		{
			fun(x,y);
		}
	}
}




function drawWorld()
{
	context.clearRect(0,0,canvasw,canvash);
	context.strokeRect(0,0,canvasw,canvash);
	
	allcells(function(x,y) {
		if (alive[y][x])
		{
			drawCell(x,y);
		}
	});
}

function createArray()
{
//	alive.length=0;
	alive = new Array(worldh);
	for ( var i = 0; i < worldh; i++) 
	{
		alive[i] = new Array(worldw);
	}
	allcells(function (x,y) {
		alive[y][x] = false;
	});
}

function clearGame()
{
	createArray();
	drawWorld();
}

var running = false;
function animate()
{
	updateLife();
	
	drawWorld();
	
	requestAnimFrame(function(){
		if (running)
		{
			animate();
		}
	})
}

function startSym()
{
	running = true;
	animate();
}

function stopSym()
{
	running = false;
}




function getWorld()
{
	window.requestAnimFrame = (function(callback) {
//		return 
//		window.requestAnimationFrame ||
//		window.webkitRequestAnimationFrame ||
//		window.mozRequestAnimationFrame ||
//		window.oRequestAnimationFrame ||
//		window.msRequestAnimationFrame ||
		return function(callback) {
			window.setTimeout(callback, 10000 / 60);
		};
	}) ();
	
	createArray();
	
	canvas=document.getElementById("gol");
	canvas.id="canvas";
	canvas.width=canvasw;
	canvas.height=canvash;
	canvas.addEventListener("click", mouseEvent, false);
	context=canvas.getContext("2d");
	
	drawWorld();
}