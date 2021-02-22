// create a file and link object
var link = "{{link}}";
var file = "{{file}}";

link = document.createElement("a"); //create 'a' element
link.setAttribute("href", link); //replace "file" with link to file you want to download
link.setAttribute("download", file);// replace "file" here too
link.click(); //virtually click <a> element to initiate download
