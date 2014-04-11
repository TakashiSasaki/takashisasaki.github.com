
$(".auth_endpoint").text(auth_endpoint);






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
