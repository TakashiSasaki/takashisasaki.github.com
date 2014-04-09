$(document).one("pagebeforecreate", function (e, ui) {

    var panel = "<div data-role='panel' id='panel'>";
    panel += '<ul data-role="listview">';
    panel += '<li><a href="index.html">ホーム</a></li>';
    panel += '<li data-role="list-divider">実験</li>';
    panel += '<li><a href="google-oauth2-js.html#installed-apps">OAuth2 for Install Apps</a></li>';
    panel += '<li><a href="google-oauth2-js.html#client-side">OAuth2 for Client-side</a></li>';
    panel += '<li><a href="google-oauth2-js.html#devices">OAuth2 for Devices</a></li>';
    panel += '</ul>';
    panel += "</div>";
    $.mobile.pageContainer.prepend(panel);
    $("#panel").panel();
    $("#panel ul").listview();
});
