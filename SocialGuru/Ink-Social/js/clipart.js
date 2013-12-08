


function loadXMLDoc(dname)
{
	if (window.XMLHttpRequest)
	  {
	  xhttp=new XMLHttpRequest();
	  }
	else
	  {
	  xhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xhttp.open("GET",dname,false);
	xhttp.send("");
	return xhttp.responseXML;
}

function searchClipart() {
	var clipartsearch=document.getElementById("clipartsearch");
	var url='/openclipart?query='+escape(clipartsearch.value);
	xml=loadXMLDoc(url);
	xsl=loadXMLDoc("/js/clipart.xsl");
	// code for IE
	if (window.ActiveXObject) {
	  ex=xml.transformNode(xsl);
	  document.getElementById("clipart").innerHTML=ex;
	}
	// code for Mozilla, Firefox, Opera, etc.
	else if (document.implementation && document.implementation.createDocument) {
	  xsltProcessor=new XSLTProcessor();
	  xsltProcessor.importStylesheet(xsl);
	  resultDocument = xsltProcessor.transformToFragment(xml,document);
	  document.getElementById("clipart").appendChild(resultDocument);
	}
}