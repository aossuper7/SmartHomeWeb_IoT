var host = "172.30.1.58";
var port = 9001;
var mqtt;
var temp;
var humid;
var lastdht;

function onConnect() {
    console.log("접속 성공");
    mqtt.subscribe("android/#");
    sendMsg('dhtget');
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
    }else if(message[1] == "pir") {
        for(let i=0; i<5; i++)
            pushNotify("error","출입 알림","침입 발생 112에 신고하세요!");
    }
//    else if(message[1] == "dhtget") {
//        lastdht = msg.payloadString.replace(/[{|}|'| ]/g,"");
//        dhtdata = lastdht.split(/[:|,]/g);
//        console.log(dhtdata);
}
function sendMsg(msg) {
    message = new Paho.MQTT.Message(msg);
    message.destinationName = "pi/dhtget";
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
