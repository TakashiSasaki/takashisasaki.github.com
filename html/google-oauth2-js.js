$("#right-panel ul").empty();
$("#right-panel ul").append('<li><a href="#page-google-oauth2-installed-apps">OAuth2 for Installed Apps</a></li>');
$("#right-panel ul").append('<li><a href="#page-google-oauth2-client-side">OAuth2 for Client-side</a></li>');
$("#right-panel ul").append('<li><a href="#page-google-oauth2-devices">OAuth2 for Devices</a></li>');
$("#right-panel ul").listview().listview("refresh");

var base_url = window.url("protocol") + "://" + window.url("hostname") + ":" +
    window.url("port") + window.url("path");

if (window.url("#access_token") != null) {
    if (window.url("#state") == "client-side") {
        $("#page-google-oauth2-client-side INPUT.token").val(window.url("#access_token"));
        setTimeout(function () {
            $(':mobile-pagecontainer').pagecontainer("change", "#client-side", {transition: 'flip', changeHash: false});
        }, 2000);
    }
}

var token_endpoint = "https://accounts.google.com/o/oauth2/token";
var auth_endpoint = "https://accounts.google.com/o/oauth2/auth";
var device_endpoint = "https://accounts.google.com/o/oauth2/device/code";

$(".auth_endpoint").text(auth_endpoint);


var native_app_client_id = "982049359064-m16bre9h586ao9q3hh08hau26v4m7c9i.apps.googleusercontent.com";
var native_app_client_secret = "4fNom33Z_nWujtQaFJzYIxjV";
var web_app_client_id = "982049359064-khobeosb81scm9kt1387mg78o399t71u.apps.googleusercontent.com";

var authorization_url_oob = auth_endpoint + "?"
    + "scope=email%20profile&"
    + "state=%2Fprofile&"
    + "redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&"
    + "response_type=code&"
    + "client_id=" + native_app_client_id;

var authorization_url_localhost = auth_endpoint + "?"
    + "scope=email%20profile&"
    + "state=%2Fprofile&"
    + "redirect_uri=http://localhost&"
    + "response_type=code&"
    + "client_id=" + native_app_client_id;

var authorization_url_web = auth_endpoint + "?"
    + "scope=email%20profile&"
    + "redirect_uri=" + encodeURIComponent(base_url) + "&"
    + "response_type=token&"
    + "client_id=" + web_app_client_id + "&"
    + "state=client-side";

$(document).on("pagecreate", function (e, ui) {
    $("#page-google-oauth2-installed-apps A.oob").attr("href", authorization_url_oob);
    $("#page-google-oauth2-installed-apps A.localhost").attr("href", authorization_url_localhost);
    $("#page-google-oauth2-client-side DIV A").attr("href", authorization_url_web);
    $("#page-google-oauth2-client-side INPUT.url").val(authorization_url_web);
});

$("#page-page-google-oauth2-installed-apps INPUT").on("keyup",
    function () {
        var data = {
            client_id: native_app_client_id,
            client_secret: native_app_client_secret,
            grant_type: "authorization_code",
            code: $("#page-page-google-oauth2-installed-apps INPUT").val(),
            redirect_uri: "urn:ietf:wg:oauth:2.0:oob"
        }
        $("#page-google-oauth2-installed-apps TEXTAREA.ajax_data").val(window.JSON.stringify(data));
        $("#page-google-oauth2-installed-apps TEXTAREA.ajax_data").keyup();
        var ajax_option = {type: "post", url: token_endpoint, data: data};
        $("#page-google-oauth2-installed-apps TEXTAREA.ajax_options").val(window.JSON.stringify(ajax_option));
        $("#page-google-oauth2-installed-apps TEXTAREA.ajax_options").keyup();
    }
);

$("#page-google-oauth2-installed-apps BUTTON.ajax_data").on("click", function () {
        var data = window.JSON.parse(
            $("#page-google-oauth2-installed-apps TEXTAREA.ajax_data").val());
        try {
            $.ajax(window.JSON.parse($("#page-google-oauth2-installed-apps TEXTAREA.ajax_options").val())).
                done(function (e) {
                    $("#access_token_result").val("done");
                }).fail(function (jqxhr, textstatus, e) {
                    $("#access_token_result").val(textstatus);
                }).always(function (e) {
                });
        } catch (e) {
            $("#access_token_result").val(e);
        }
    }
);

$("#page-google-oauth2-devices button").on("click", function () {
    var data = {
        client_id: native_app_client_id,
        scope: "email profile"
    }
    $.ajax({type: "post", url: device_endpoint, data: data, dataType: "json"}).done(function (j) {
        $("#page-google-oauth2-devices input.device_code").val(j.device_code);
        $("#page-google-oauth2-devices input.user_code").val(j.user_code);
    });
});
