__author__ = 'Takashi SASAKI'
import http.server
import logging
import cgi
import json
import urllib.parse
import urllib.request
import urllib.response
import http.client
import ssl


def do_GET(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.end_headers()
    page = """
    <html><head></head><body>
    <form action="/proxy" method="POST">
        <textarea name="ajax_options" cols="60" rows="10">
            {
                "type": "get",
                "url":"http://www.yahoo.co.jp/?a=b#c=d",
                "data": {
                    "param1":"value1",
                    "param2":"value2"
                }
            }
        </textarea>
        <button type="submit">submit</button>
    </form>
    <form action="/proxy" method="POST">
        <textarea name="ajax_options" cols="60" rows="10">
            {
                "type": "get",
                "url":"https://www.yahoo.com/?a=b#c=d",
                "data": {
                    "param1":"value1",
                    "param2":"value2"
                }
            }
        </textarea>
        <button type="submit">submit</button>
    </form>
    <form action="/proxy" method="POST">
        <textarea name="ajax_options" cols="60" rows="10">
            {
                "type": "post",
                "url":"http://www.yahoo.co.jp/?a=b#c=d",
                "data": {
                    "param1":"value1",
                    "param2":"value2"
                }
            }
        </textarea>
        <button type="submit">submit</button>
    </form>
    <form action="/proxy" method="POST">
        <textarea name="ajax_options" cols="60" rows="10">
            {
                "type": "post",
                "url":"https://www.yahoo.com/?a=b#c=d",
                "data": {
                    "param1":"value1",
                    "param2":"value2"
                }
            }
        </textarea>
        <button type="submit">submit</button>
    </form>
    </body></html>
    """
    self.wfile.write(bytes(page, "UTF-8"))


def do_POST(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    #self.send_response(200)
    #self.send_header("Content-Type", "text/plain")
    #self.end_headers()
    #self.wfile.write(bytes("proxy.py", "UTF-8"))
    body_len = int(self.headers['Content-Length'])
    logging.info(body_len)
    logging.info(self.headers["Content-Type"])
    body = self.rfile.read(body_len)
    decoded_body = cgi.parse_qs(body)
    json_bytes = decoded_body.get(b"ajax_options")[0]
    json_string = json_bytes.decode("UTF-8")
    logging.info(json_string)
    decoded_json = json.loads(json_string)
    proxy_post(self, decoded_json)
    #self.wfile.write(bytes(decoded_json["url"], "UTF-8"))


def proxy_post(self, ajax_options):
    parsed_url = urllib.parse.urlparse(ajax_options["url"])
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
        http_connection = http.client.HTTPSConnection(netloc, port, context=context)

    query_from_url = cgi.parse_qs(query)
    for k in query_from_url.keys():
        query_from_url[k] = query_from_url[k][0]
    query_from_ajax_options = ajax_options.get("data")
    query_merged = {}
    query_merged.update(query_from_url)
    query_merged.update(query_from_ajax_options)

    if ajax_options.get("type") in ["GET", "get"]:
        if len(query_merged) > 0:
            url = path + "?" + urllib.parse.urlencode(query_merged)
            http_connection.request("GET", url)
        else:
            http_connection.request("GET", path)

    if ajax_options.get("type") in ["POST", "post"]:
        if len(query_from_url) > 0:
            url = path + "?" + urllib.parse.urlencode(query_from_url)
            body = urllib.parse.urlencode(query_from_ajax_options)
            http_connection.request("POST", url, body)
        else:
            body = urllib.parse.urlencode(query_from_ajax_options)
            http_connection.request("POST", path, body)

    http_response = http_connection.getresponse()
    assert isinstance(http_response, http.client.HTTPResponse)
    logging.info("status = %s" % http_response.status)
    #self.send_response(http_response.status)
    self.send_response(http_response.status)
    for k in http_response.headers:
        self.send_header(k, http_response.getheader(k))
    self.end_headers()
    self.wfile.write(http_response.read())