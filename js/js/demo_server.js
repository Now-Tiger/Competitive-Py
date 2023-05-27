#!/usr/bin/env node

var http = require('http');
var dt = require('./dateTime');

http.createServer(
    function(request, results) {
        results.writeHead(200, {'Content-Type' : 'text/plain'});
        results.end(`The date & time are currently: ${dt.myDate()}`);
    }
).listen(8080);