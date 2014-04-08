$(document).one("pagebeforecreate", function (e, ui) {

    var panel = "<div data-role='panel' id='panel'>";
    panel += '<ul data-role="listview">';
    panel += '<li><a href="index.html">ホーム</a></li>';
    panel += '<li data-role="list-divider">実験</li>';
    panel += '<li><a href="google-oauth2-js.html">OAuth2実験１</a></li>';
    panel += '</ul>';
    panel += "</div>";
    $.mobile.pageContainer.prepend(panel);
    $("#panel").panel();
    $("#panel ul").listview();
});
