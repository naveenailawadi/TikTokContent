// create a file and link object
var link = "{{link}}";
var file = "{{file}}";

elem = document.createElement("a"); //create 'a' element
elem.setAttribute("href", link); //replace "file" with link to file you want to download
elem.setAttribute("target", "_blank");
elem.setAttribute("download", file);// replace "file" here too
elem.click(); //virtually click <a> element to initiate download
