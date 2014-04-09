__author__ = 'Takashi SASAKI'
import http.server
import logging
import cgi
import json
import urllib.parse
import http.client
import ssl


def do_GET(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.end_headers()
    page = """
    <html>
    <head></head>
    <body><form action="/proxy" method="POST">
    <textarea name="ajax_option" cols="60" rows="10">
        {
            "type": "get",
            "url":"http://localhost?a=b#c=d",
            "data": {
                "param1":"value1",
                "param2":"value2"
            }
        }
    </textarea>
    <button type="submit">submit</button>
    </form>
    <script></script>
    </body>
    </html>
    """
    self.wfile.write(bytes(page, "UTF-8"))


def do_POST(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.send_response(200)
    self.send_header("Content-Type", "text/plain")
    self.end_headers()
    #self.wfile.write(bytes("proxy.py", "UTF-8"))
    body_len = int(self.headers['Content-Length'])
    logging.info(body_len)
    logging.info(self.headers["Content-Type"])
    body = self.rfile.read(body_len)
    decoded_body = cgi.parse_qs(body)
    json_bytes = decoded_body[b"ajax_option"][0]
    json_string = json_bytes.decode("UTF-8")
    logging.info(json_string)
    decoded_json = json.loads(json_string)
    proxy_post(self, decoded_json)
    self.wfile.write(bytes(decoded_json["url"], "UTF-8"))


def proxy_post(self, ajax_option):
    parsed_url = urllib.parse.urlparse(ajax_option["url"])
    scheme = parsed_url.scheme
    netloc = parsed_url.netloc
    path = parsed_url.path
    params = parsed_url.params
    query = parsed_url.query
    fragment = parsed_url.fragment
    username = parsed_url.username
    password = parsed_url.password
    hostname = parsed_url.hostname
    port = parsed_url.port
    if scheme == "http" or scheme == "HTTP":
        if port is None:
            port = 80
        http_connection = http.client.HTTPConnection(netloc, port)
    if scheme == "https" or scheme == "HTTPS":
        if port is None:
            port = 443
        context = ssl.create_default_context()
        http_connection = http.client.HTTPConnection(netloc, port, context=context)

    http_connection.request(ajax_option.type, "/" + ajax_option.path)