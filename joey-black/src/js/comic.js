var canvas;
var context;

var canvasw=1000;
var canvash=450;

var key;

// the sequence of the right most frame
// eg 1x1x2 is the 2nd version of the 3rd frame
var rframeseq;

var numFrames=3;

var ctxroot="http://joey-black.appspot.com";
//var ctxroot="http://localhost:8080";

//+ Jonas Raoni Soares Silva
//@ http://jsfromhell.com/string/wordwrap [v1.0]

String.prototype.wordWrap = function(m, b, c){
    var i, j, s, r = this.split("\n");
    if(m > 0) for(i in r){
        for(s = r[i], r[i] = ""; s.length > m;
            j = c ? m : (j = s.substr(0, m).match(/\S*$/)).input.length - j[0].length
            || m,
            r[i] += s.substr(0, j) + ((s = s.substr(j)).length ? b : "")
        );
        r[i] += s;
    }
    return r.join("\n");
};

// end Jonas code



function Point(x, y) {
    this.x=x;
    this.y=y;
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

function setRframeseq(rframeseq) {
  var rfs=document.getElementById("rframeseq");
  rfs.value=rframeseq
}

function last() {
	location.href="/comic?go=last&comickey="+key;
}

function left() {
  var l=rframeseq.length;
	if (l>=3) {
	  rframeseq=rframeseq.substring(0,l-2);
	}
	else {
	  rframeseq=rframeseq.substring(0,1);
	}
	
	setRframeseq(rframeseq);
	
	drawFrames();
}

function jumpleft() {
  var l=rframeseq.length;
  if (l>=7) {
    rframeseq=rframeseq.substring(0,l-6);
  }
  else {
    rframeseq=rframeseq.substring(0,1);
  }
  
  setRframeseq(rframeseq);
  
  drawFrames();
}

function right() {
	rframeseq+="x1";
	
  setRframeseq(rframeseq);
	
	drawFrames();
}

function jumpright() {
  rframeseq+="x1x1x1";
  
  setRframeseq(rframeseq);
  
  drawFrames();
}

function next() {
	location.href="/comic?go=next&comickey="+key;
}


function up() {
  var l=rframeseq.length;
  rframeseq=rframeseq.substring(0,l-1) + (parseInt(rframeseq.substring(l-1,l)) - 1);

  setRframeseq(rframeseq);
  
  drawRightFrame();
}

function down() {
  var l=rframeseq.length;
  rframeseq=rframeseq.substring(0,l-1) + (parseInt(rframeseq.substring(l-1,l)) + 1);

  setRframeseq(rframeseq)
  
  drawRightFrame();  
}

function mouseEvent(e) {
    var point=getCursorPosition(e);
    
    if (point.x>=0 && point.x<25) {
    	last();
    }
    else if (point.x>50 && point.x<350) {
    	left();
    }
    else if (point.x>25 && point.x<50) {
      jumpleft();
    }
    else if (point.x>=650 && point.x<950 && point.y>25 && point.y<425) {
    	right();
    }
    else if (point.x>=950 && point.x<975) {
      jumpright();
    }
    else if (point.x>=975 && point.x<1000) {
    	next();
    }
    else if (point.x>=650 && point.y<=25) {
      up();
    }
    else if (point.x>=650 && point.y>=425) {
      down();
    }
}


function drawNav() {
  var sideShift=200;
  var rightShift=775;
  
	// last
	context.fillStyle    = '#00f';
	context.font         = 'bold 20px sans-serif';
	context.translate(20, sideShift);
	context.rotate(-90 * Math.PI/180);
	context.fillText("last comic", 0, 0);
	
	context.rotate(90 * Math.PI/180);
	context.translate(-20, sideShift*-1);
	
	//left
	context.translate(50, sideShift);
	context.rotate(-90 * Math.PI/180);
	context.translate(0, 0);
	context.fillText("scroll left", 0, -5);
	
	context.rotate(90 * Math.PI/180);
	context.translate(-50, sideShift*-1);
	
	//next
	context.fillStyle    = '#00f';
	context.font         = 'bold 20px sans-serif';
	context.translate(980, sideShift);
	context.rotate(90 * Math.PI/180);
	context.fillText("next comic", 0, 0);
	
	context.rotate(-90 * Math.PI/180);
	context.translate(-980, sideShift*-1);
	
	//right
	context.translate(950, sideShift);
	context.rotate(90 * Math.PI/180);
	context.translate(0, 0);
	context.fillText("scroll right", 0, -5);
	
	context.rotate(-90 * Math.PI/180);
	context.translate(-950, sideShift*-1);
	
	//up
	context.fillText("up", rightShift, 18);
	
	//down
	context.fillText("down", rightShift, 442);
}

function drawBorder(x, y) {
	context.strokeRect(x,y,300,400);
}





function getRequest(myurl) {
	var response;
	var xmlhttp;
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  	xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  	xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	
	xmlhttp.open("GET",myurl,false); 
	xmlhttp.send(); 
	
	//while ( (xmlhttp.readyState!=4 || xmlhttp.status!=200) && xmlhttp.status<200){}
	if (xmlhttp.readyState==4 && xmlhttp.status==200) {
		response=xmlhttp.responseText;
	}
	
	return response;
}


function getText(fnum) {
	var url=ctxroot+"/frame?type=text&key="+key+"&fnum="+fnum+"&rframeseq="+rframeseq;
	var text=getRequest(url);
	return text;
}

function getImg(fnum) {
  var img=new Image();
  img.src="/frame?type=image&key="+key+"&fnum="+fnum+"&rframeseq="+rframeseq;

	return img;
}




function drawFrame(fnum, text, img) {
	var x=50;
	var y=25;
	if (fnum>1) {
		x+=300;
	}
	if (fnum>2) {
		x+=300;
	}
	
	// Text
	context.fillStyle    = '#000';
	context.font         = '15px sans-serif';
	var charsPerLine=38;
	lines=text.wordWrap(charsPerLine, "\n", false).split("\n");
	var y2=20; // shift text down
	var x2=3;
	for(i in lines) {
		context.fillText(lines[i], x+x2, y+y2);
		y2+=16;
	}
	
	//image
	if (img!=null)
	{
		img.onload = function() {
			context.drawImage(img, x+5, y+100);
		}
	}
	
	drawBorder(x,y);
}


function drawFrames() {
	context.clearRect(49, 24, 902, 402);
	
	var text=new Array();
	var img=new Array();
	
	//for each frame, get/draw
	for (var i=1; i<=numFrames; i++) {
			text[i]=getText(i);
			img[i]=getImg(i);
      if (text[i]!=null || img[i]!=null) {
        drawFrame(i, text[i], img[i]);
      }
	}
	
	//for each frame, draw
  /*for (var i=1; i<=numFrames; i++) {
      if (text[i]!=null || img[i]!=null) {
        drawFrame(i, text[i], img[i]);
      }
  }*/
	
}

function drawRightFrame() {
  context.clearRect(649, 24, 302, 402);
  var text=getText(numFrames);
  var img=getImg(numFrames);
  if (text!=null || img!=null) {
    drawFrame(numFrames, text, img);
  }
}



function getComic(k, f) {
	key=k;
	rframeseq=f;
	canvas=document.getElementById("comic");
	canvas.id="canvas";
	//document.body.appendChild(canvas);
	canvas.width=canvasw;
	canvas.height=canvash;
	canvas.addEventListener("click", mouseEvent, false);
	context=canvas.getContext("2d");
	//context.strokeRect(0,0,canvasw,canvash);
	drawNav();
	drawFrames();
}


function deleteFrame() {

	var url=ctxroot+"/frame?type=delete&key="+key+"&fnum="+3+"&rframeseq="+rframeseq;
	
	var r=confirm("Delete frame on right?");
	
	if (r==true) {
		getRequest(url);
		//drawFrames();
		left();
	}
}

function deleteComic() {

	var url=ctxroot+"/comic?type=delete&comickey="+key;
	
	var r=confirm("Delete this comic?");
	
	if (r==true) {
		location.href=url;
	}
}

