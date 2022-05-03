var state = 0

var state = 0;
function onConnect(){
    console.log("연결완료")
    mqtt.subscribe("iot/#")
}

function onMessageArrived(msg){
    topic = msg.destinationName.split('/')
    if(topic[1] == "camera"){
    document.getElementById("myimg").src = "data:image/jpeg;base64,"+btoa(String.fromCharCode.apply(null,msg.payloadBytes))
    }
}
function onFailure(){
    console.log("연결실패");
    setTimeout(MQTTConnect,reconnectTimeout);
}
function sendMsg(msg){
  message = new Paho.MQTT.Message(msg);
  message.destinationName = "camerachk"
  mqtt.send(message);
}
function MQTTConnect(){
    mqtt = new Paho.MQTT.Client(host,port,"streaming");
    var options = {
        timeout:3,
        onSuccess : onConnect,
        onFailure : onFailure,
    }
    mqtt.onMessageArrived = onMessageArrived;
    mqtt.connect(options);
}

//function CctvOnOff() {
//    if (state == 0){
//        document.getElementById('cctv').value = "CCTV On";
//        sendMsg("stop")
//        }
//    else if (state == 1){
//        document.getElementById('cctv').value = "CCTV Off";
//        sendMsg("start")}
//
//    state = !state
//};
function CctvOnOff() {
    if (document.getElementById('cctv').value == "CCTV On"){
        document.getElementById('cctv').value = "CCTV Off";
        sendMsg("start")
        }
    else if (document.getElementById('cctv').value == "CCTV Off"){
        document.getElementById('cctv').value = "CCTV On";
        sendMsg("stop")
        setTimeout(function() {
          document.getElementById('myimg').src ="static/img/cctvwait.png"
        }, 100);
        }
    state = !state
};

function cctvinit() {
    window.onbeforeunload = function (e) {
            document.getElementById('cctv').value = "CCTV On";
            sendMsg("stop")
    };
}