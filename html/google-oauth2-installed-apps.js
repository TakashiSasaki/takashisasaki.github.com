$("#google-oauth2-installed-apps").on("pagecreate", function () {
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

    $("#google-oauth2-installed-apps A.oob").attr("href", authorization_url_oob);
    $("#google-oauth2-installed-apps A.localhost").attr("href", authorization_url_localhost);

    $("#google-oauth2-installed-apps INPUT").on("keyup",
        function () {
            var data = {
                client_id: native_app_client_id,
                client_secret: native_app_client_secret,
                grant_type: "authorization_code",
                code: $("#google-oauth2-installed-apps INPUT").val(),
                redirect_uri: "urn:ietf:wg:oauth:2.0:oob"
            }
            $("#google-oauth2-installed-apps TEXTAREA.ajax_data").val(window.JSON.stringify(data));
            $("#google-oauth2-installed-apps TEXTAREA.ajax_data").keyup();
            var ajax_option = {type: "post", url: token_endpoint, data: data};
            $("#google-oauth2-installed-apps TEXTAREA.ajax_options").val(window.JSON.stringify(ajax_option));
            $("#google-oauth2-installed-apps TEXTAREA.ajax_options").keyup();
        }
    );

    $("#google-oauth2-installed-apps BUTTON.ajax_data").on("click", function () {
            var data = window.JSON.parse(
                $("#google-oauth2-installed-apps TEXTAREA.ajax_data").val());
            try {
                $.ajax(window.JSON.parse($("#google-oauth2-installed-apps TEXTAREA.ajax_options").val())).
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

});


