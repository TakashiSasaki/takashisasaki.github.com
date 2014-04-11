$(document).one("pagecreate", function (e, ui) {
    //alert("pagebeforecreate");
    $("#left-panel ul").append('<li data-role="list-divider">めにう</li>');
    $("#left-panel ul").append('<li><a href="index.html">ホーム</a></li>');
    $("#left-panel ul").append('<li><a href="google-oauth2-client-side.html">OAuth2 for JavaScript Apps</a></li>');
    $("#left-panel ul").append('<li><a href="google-oauth2-installed-apps.html">OAuth2 for Installed Apps</a></li>');
    $("#left-panel ul").append('<li><a href="google-oauth2-devices.html">OAuth2 for Devices</a></li>');
    $("#left-panel ul").append('<li><a href="google-drive.html">Google Drive API Demo</a></li>');
    $("#left-panel ul").append('<li><a href="offline-content.html">Offline Content Demo</a></li>');
    $("#left-panel ul").append('<li><a href="test.html">test</a></li>');
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
