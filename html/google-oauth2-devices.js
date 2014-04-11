$("#google-oauth2-devices").on("pagecreate", function (e, ui) {
    $("#google-oauth2-devices BUTTON").on("click", function () {
        var data = {
            client_id: native_app_client_id,
            scope: "email profile"
        }
        $.ajax({type: "post", url: device_endpoint, data: data, dataType: "json"}).done(function (j) {
            $("#google-oauth2-devices INPUT.device_code").val(j.device_code);
            $("#google-oauth2-devices INPUT.user_code").val(j.user_code);
        });
    });
});
