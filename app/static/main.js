function copyToClip(contentArray, message) {
    var contents = "";
    for (var i = 0; i < contentArray.length; i++) {
        contents += contentArray[i] + "\n";
    }
    const textarea = document.createElement('textarea');
    textarea.value = contents;
    document.body.appendChild(textarea);
    textarea.select();
    if (document.execCommand('copy')) {
        document.execCommand('copy');
    }
    document.body.removeChild(textarea);
    if (message == null) {
        alert("复制成功！\n期待您的推荐！");
    } else {
        alert(message);
    }
}

function show_QRcode() {
    url = window.location.href;
    document.getElementById("result").style.display = "none"
    document.getElementById("qrcode").style.display = "inline"
    new QRCode(document.getElementById("img"), url);	
}
