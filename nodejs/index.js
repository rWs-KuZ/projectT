var http = require("http")

http.createServer(function (request,response){
    response.writeHead(200, {'Content-Type': 'text/plain'})
    response.end('Hello World\n');
}).listen(12138)

console.log('hello world, running on http://localhost:12138/')