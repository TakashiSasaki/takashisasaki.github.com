$("#google-oauth2-client-side").on("pagecreate", function (e, ui) {
    var redirect_uri = window.url("protocol") + "://" + window.url("hostname") + ":" +
        window.url("port") + "/" + window.url(1) + "/html/google-oauth2-client-side.html";

    var authorization_url_web = auth_endpoint + "?"
        + "scope=email%20profile&"
        + "redirect_uri=" + encodeURIComponent(redirect_uri) + "&"
        + "response_type=token&"
        + "client_id=" + web_app_client_id + "&"
        + "state=hello%20world%20state";

    $("#google-oauth2-client-side DIV A").attr("href", authorization_url_web);
    $("#google-oauth2-client-side INPUT.url").val(authorization_url_web);

    var token = localStorage.getItem("google-oauth2-client-side-token");
    if (token) {
        $("#google-oauth2-client-side INPUT.token").val(token);
    }

});
