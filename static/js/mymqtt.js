var host = "192.168.50.201";
var port = 9001;
var mqtt;
var temp;
var humid;

function onConnect() {
    console.log("접속 성공");
    mqtt.subscribe("android/#");
}
function onFailure() {
    console.log("접속 실패");
}
function onMessageArrived(msg) {
    message = msg.destinationName.split("/");
    if(message[1] == "rfid") {
        pushNotify("success","출입 알림",msg.payloadString+"님이 들어왔습니다");
    }else if(message[1] == "dht") {
        data = msg.payloadString.split(":");
        humid = data[1];
        temp = data[2];
        $.ajax({
            type:"GET",
            url:"/dataset",
            data:{"humid":humid,
                  "temp":temp}
        })
    }
}
function sendMsg(msg) {
    message = new Paho.MQTT.Message(msg);
    message.destinationName = "pi/dht";
    mqtt.send(message);
}
function MQTTConnect() {
    console.log("mqtt접속"+host+","+port);
    mqtt = new Paho.MQTT.Client(host, port,"javascript_client");
    var options = {
        timeout:3,
        onSuccess:onConnect,
        onFailure:onFailure,
    }
    mqtt.onMessageArrived = onMessageArrived;
    mqtt.connect(options);
}

MQTTConnect();