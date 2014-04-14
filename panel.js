$(document).one("pagecreate", function (e, ui) {
    //alert("pagebeforecreate");
    //$.mobile.pageContainer.append(panel);
    //$.mobile.pageContainer.prepend(panel);
    //$("body").append(panel)
    $("#left-panel").append('<div id="script-buffer"></div>');
    $("#left-panel").panel();
    $("#left-panel ul").listview();
    $("#right-panel").panel({ dismissible: false });
    $("#right-panel ul").listview();

    localhostPingCallback();
});

function localhostPingCallback(e) {
    setTimeout(function () {
        $("#script-buffer").empty();
        $("#script-buffer").append('<script src="http://localhost/?callback=localhostPingCallback"></script><div><p>localhost最終確認</p><p>' + $.timeago(new Date()) + '</p></div>');
        $("#panel").panel();
    }, 10000);
}
