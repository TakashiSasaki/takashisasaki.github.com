__author__ = 'Takashi SASAKI'
import http.server
import logging
import cgi


def do_GET(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.end_headers()
    page = """
    <html>
    <head></head>
    <body><form action="/proxy" method="POST">

    <textarea name="ajax" placeholder="{}" cols="60" rows="10"></textarea>
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
    logging.info(decoded_body)
    self.wfile.write(decoded_body[b"ajax"][0])
