#!/usr/bin/env node

var http = require('http')

http.createServer(function(request, result) {
    result.write("Hello client");
    result.end();
}).listen(8080);

