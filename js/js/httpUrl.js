#!/usr/bin/env node

var http = require('http');

http.createServer(
    function(request, result) {
        result.writeHead(200, {'Content-Type' : 'text/html'});
        result.write(request.url);
        result.end();
    }
).listen(8080);

/* http://localhost:8080/summer */