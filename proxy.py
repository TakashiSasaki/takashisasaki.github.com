__author__ = 'Takashi SASAKI'
import http.server


def do_GET(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.end_headers()
    page = """
    <html>
    <head></head>
    <body><form action="/proxy" method="POST">

    <textarea placeholder="{}" cols="60" rows="10"></textarea>
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
    self.wfile.write(bytes("proxy.py", "UTF-8"))
