
var state = 0;

function CctvOnOff() {
    if (document.getElementById('cctv').value == "CCTV On"){
        document.getElementById('cctv').value = "CCTV Off";
        sendMsg("camerachk","start")
        }
    else if (document.getElementById('cctv').value == "CCTV Off"){
        document.getElementById('cctv').value = "CCTV On";
        sendMsg("camerachk","stop")
        setTimeout(function() {
          document.getElementById('myimg').src ="static/img/cctvwait.png"
        }, 500);
        }
    state = !state
};
function sendMsg(topic, msg){
          message = new Paho.MQTT.Message(msg);
          message.destinationName = topic
          mqtt.send(message);
        }
function cctvinit() {
    window.onbeforeunload = function (e) {
        document.getElementById('cctv').value = "CCTV On";
        sendMsg("camerachk","stop")
        setTimeout(function() {
          document.getElementById('myimg').src ="static/img/cctvwait.png"
        }, 500);
    };
}