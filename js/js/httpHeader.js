#!/usr/bin/env node

var http = require('http');

http.createServer(
    function(request, results) {
        results.writeHead(200, {'Content-Type' : 'text/plain'});
        results.write("Hello Client");
        results.end();
    }
).listen(8080);