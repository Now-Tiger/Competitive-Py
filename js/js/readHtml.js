#!/usr/bin/env node

var http = require('http');

// The Node.js file system module allows you to work with the file system 
// on your computer.
var fs = require('fs');

http.createServer(function (request, result) {
    fs.readFile('../html/demo.html', function (err, data) {
        result.writeHead(200, { 'Content-Type': 'text/html' });
        result.write(data);
        return result.end();
    });
}).listen(8080);

/* localhost:8080/   renders given html file.  */