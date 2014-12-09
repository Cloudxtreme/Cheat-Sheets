Socket IO
aprendido:
	Al conectarse se debe obtener el session id del request y luego hacerle join
	para obtener el session id se puede usar io.use, de esta forma al conectarse
	el cliente inmediatamente lo tenemos en sesion.
client:
	var socket = io();
	socket.on('widget', function (data) {
				console.log('widget received');
			});
server:
	io.to(id).emit(xxx)	: emite mensaje a session id
	
Notas: 
	se require usar https (http+ssl) para proxies se recomienda nginx
	

http://social.technet.microsoft.com/wiki/contents/articles/21711.aplicaciones-en-tiempo-real-html5-y-node-js-es-es.aspx
Crear un html que se conectará a un servidor el cual recibirá los mensajes y devolverá el eco,

~~~html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title></title>
</head>
<body>
    <input id="Message" type="text" name="name" value=""/>
    <button type="button" id="Send">Enviar</button><br/>
    <div id="Messages"></div>  <!-- here we will show the messages -->
    <script>
        var WebSocket = new WebSocket("ws://echo.websocket.org");

        WebSocket.addEventListener("open", function () {
            console.log("Conectado");
        });

        WebSocket.addEventListener("message", function (message) {
            document.getElementById("Messages").innerHTML += message.data + "<br />";
        });

        document.getElementById("Send").addEventListener("click", function () {
            socket.send(document.getElementById("Message").value);
        });
    </script>
</body>
</html>
~~~

En la pestaña Network podemos visualizar si la Url de los WebSockets se ha cargado perfectamente mediante el "Status Code", el 101

Instsall Socket.io
    npm install socket.io

server.js
~~~javascript
var io = require('socket.io').listen(3000);
io.sockets.on('connection', function (socket) {
    socket.on('message', function (mensaje) {
        io.sockets.send(mensaje);
    });
});
~~~




Lo mismo pero con Emit

~~~javascript
var io = require('socket.io').listen(3000);
io.sockets.on('connection', function (socket) {
    socket.on('mensaje_cliente', function (mensaje) {
        io.sockets.emit("mensaje_servidor", mensaje);
    });
});
~~~

~~~html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title></title>
</head>
<body>
    <input id="Message" type="text" name="name" value=""/>
    <button type="button" id="Send">Enviar</button><br/>
    <div id="Messages"></div>
    <script src="http://localhost:3000/socket.io/socket.io.js"></script>
    <script type="text/javascript">
        socket = io.connect("http://localhost:3000");
        socket.on("connect", function () {
            console.log("Conectado");
        });
        socket.on("mensaje_servidor", function (message) {
            document.getElementById("Messages").innerHTML += message + "<br />";
        });
        document.getElementById("Send").addEventListener("click", function () {
            socket.emit("mensaje_cliente", document.getElementById("Message").value);
        });
    </script>
</body>
</html>
~~~