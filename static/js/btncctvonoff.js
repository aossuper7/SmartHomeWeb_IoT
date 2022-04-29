var state = 0
function CctvOnOff() {
    if (state == 0)
        document.getElementById('cctv').value = "CCTV On";
    else if (state == 1)
        document.getElementById('cctv').value = "CCTV Off";

    state = !state
};