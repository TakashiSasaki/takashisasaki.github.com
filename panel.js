$(document).one("pagebeforecreate", function (e, ui) {

    var panel = "";
    panel += '<ul data-role="listview">';
    panel += '<li><a href="index.html">ホーム</a></li>';
    panel += '<li data-role="list-divider">実験</li>';
    panel += '<li><a href="google-oauth2-js.html#installed-apps">OAuth2 for Installed Apps</a></li>';
    panel += '<li><a href="google-oauth2-js.html#client-side">OAuth2 for Client-side</a></li>';
    panel += '<li><a href="google-oauth2-js.html#devices">OAuth2 for Devices</a></li>';
    panel += '<li><a href="html/google-drive.html#google-drive-api-demo">Google Drive API Demo</a></li>';
    panel += '</ul>';
    panel += "";
    //$.mobile.pageContainer.append(panel);
    //$.mobile.pageContainer.prepend(panel);
    $("#panel").append(panel);
    //$("body").append(panel);
    $("#panel").panel();
    $("#panel ul").listview();
});
