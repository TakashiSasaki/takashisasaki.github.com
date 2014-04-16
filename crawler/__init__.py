__author__ = 'Takashi SASAKI'
import http.server


def do_POST(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.wfile.write(bytes("do_GET", "UTF-8"))
    pass


def do_GET(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.wfile.write(bytes("do_GET", "UTF-8"))
    pass