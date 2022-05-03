
var state = 0;

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