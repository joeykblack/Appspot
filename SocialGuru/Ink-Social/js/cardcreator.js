// Card creation html5 script


var pagewidth = 700;
var pageheight = 885;
var cardwidth = pagewidth/2;
var cardheight = pageheight/2;
var layer;
var stage;
var cardbackground;
var selected = null;
var curTextColor = '000000';

function showFront() {
	alert('test');
}

function showInsideLeft() {
	alert('test');
}

function showInsideRight() {
	alert('test');
}

function showBack() {
	alert('test');
}


// background

function backgroundColorChanged() {
	var color=document.getElementById("backgroundcolor");
	cardbackground.setFill(color.value);
    stage.draw();
}


// text

function deleteSelected() {
	if (selected!=null) {
		selected.hide();
	    stage.draw();
	}
}

function ontextChange() {
	if (selected!=null) {
		var newtext=document.getElementById("newtext");
		selected.setText(newtext.value);
		stage.draw();
	}
}

function clearSelected() {
	selected = null;
	var newtext=document.getElementById("newtext");
	newtext.value='';
}

function textColorChanged() {
	var color=document.getElementById("textcolor");
	curTextColor = color.value;
	if (selected!=null) {
		selected.setTextFill(curTextColor);
	}
    stage.draw();
}

function addText() {
	var newtext=document.getElementById("newtext");
	var simpleText = new Kinetic.Text({
        x: stage.getWidth() / 2,
        y: 50,
        text: newtext.value,
        fontSize: 30,
        fontFamily: "Calibri",
        textFill: curTextColor,
        align: "center",
        verticalAlign: "middle",
        draggable: true
      });
	selected = simpleText;
	simpleText.on('click', function(evt) {
	    selected = simpleText;
	    var color=document.getElementById("textcolor");
	    color.value=selected.getTextFill();
	    color.color.fromString(color.value)
	    var newtext=document.getElementById("newtext");
	    newtext.value=selected.getText();
	  });
	simpleText.on("mouseover", function() {
        document.body.style.cursor = "pointer";
      });
	simpleText.on("mouseout", function() {
        document.body.style.cursor = "default";
      });
	layer.add(simpleText);
    stage.draw();
}



// Save

function saveCard() {
	var json = stage.toJSON();
	// TODO: send json to server
}



window.onload = function() {
    stage = new Kinetic.Stage({
      container: "card",
      width: cardwidth,
      height: cardheight,
      strokeWidth: 1,
      stroke: "black"
    });
    layer = new Kinetic.Layer();
    
    cardbackground = new Kinetic.Rect({
        x: 0,
        y: 0,
        width: cardwidth,
        height: cardheight,
        fill: "#FFFFFF"
      });

    // add the shape to the layer
    layer.add(cardbackground);
    
    stage.add(layer);
}


