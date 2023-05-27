#!/usr/bin/env node

var http = require('http')
var url = require('url');

http.createServer(
    function (request, result) {
        result.writeHead(200, { 'Content-Type': 'text/html' });
        var q = url.parse(request.url, true).query;
        var txt = `${q.year} ${q.month}`;
        result.end(txt)
    }
).listen(8080);

/* http://localhost:8080/?year=2017&month=july  <- browser */