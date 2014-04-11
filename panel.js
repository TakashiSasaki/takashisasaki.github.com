$(document).one("pagebeforecreate", function (e, ui) {

    var panel = "";
    panel += '<ul data-role="listview">';
    panel += '<li><a href="index.html">ホーム</a></li>';
    panel += '<li data-role="list-divider">実験</li>';
    panel += '<li><a href="google-oauth2-js.html#installed-apps">OAuth2 for Installed Apps</a></li>';
    panel += '<li><a href="google-oauth2-js.html#client-side">OAuth2 for Client-side</a></li>';
    panel += '<li><a href="google-oauth2-js.html#devices">OAuth2 for Devices</a></li>';
    panel += '<li><a href="google-drive.html">Google Drive API Demo</a></li>';
    panel += '<li><a href="offline-content.html">Offlinet Content Demo</a></li>';
    panel += '</ul>';
    panel += '<div id="script-buffer"></div>';
    panel += "";
    //$.mobile.pageContainer.append(panel);
    //$.mobile.pageContainer.prepend(panel);
    $("#panel").append(panel);
    //$("body").append(panel);
    $("#panel").panel();
    $("#panel ul").listview();

    localhostPingCallback();
});

function localhostPingCallback(e) {
    setTimeout(function () {
        $("#script-buffer").empty();
        $("#script-buffer").append('<script src="http://localhost/?callback=localhostPingCallback"></script><div><p>localhost最終確認</p><p>' + $.timeago(new Date()) + '</p></div>');
        $("#panel").panel();
    }, 10000);
}
