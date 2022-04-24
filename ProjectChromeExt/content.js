
websocket = new WebSocket("ws://localhost:23048/");
websocket.addEventListener("open", function(event) {
    if (window.location.hostname=="www.youtube.com") 
        websocket.send(window.location.href);
});
websocket.addEventListener("message", function(event) {
    console.log(event.data);
});