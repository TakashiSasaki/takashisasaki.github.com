var CLIENT_ID = "982049359064-khobeosb81scm9kt1387mg78o399t71u.apps.googleusercontent.com";
var SCOPES = [
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
    // Add other scopes needed by your application.
];
function handleClientLoad() {
    gapi.client.load('drive', 'v2');
    google.load('visualization', '1', {packages: ['table', 'corechart'], callback: function () {
        }}
    );
    var access_token = localStorage.getItem("access_token");
    if (access_token) {
        gapi.auth.setToken(access_token);
    }
    $("#google-drive BUTTON.auth").on("click",
        function () {
            authenticate();
            return false;
        }
    );
    $("#google-drive BUTTON.list").on("click",
        function () {
            var request = gapi.client.drive.files.list();
            request.execute(function (resp) {
                items = resp.items;
                var data = new google.visualization.DataTable();
                data.addColumn("string", "title");
                if (items) {
                    items.forEach(function (x) {
                        data.addRow([x.title]);
                    });
                }
                var table = new google.visualization.Table(document.getElementById("file-list-table"));
                table.draw(data, {showRowNumber: true});
            });
        }
    )
}

function authenticate() {
    localStorage.removeItem("gapi_oauth2_token");
    gapi.auth.authorize({client_id: CLIENT_ID, scope: SCOPES.join(' '), immediate: false},
        function () {
            var gapi_oauth2_token = gapi.auth.getToken();
            localStorage.setItem("access_token", gapi_oauth2_token.access_token);
        }
    );
}

