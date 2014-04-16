__author__ = 'Takashi SASAKI'
import http.server
#import cgi


def do_GET(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.send_header("Content-Type", "text/html; charset=UTF-8")
    self.wfile.write(bytes("""<html><head><title></title></head><body>
    <form method="POST" action="crawler/walk">
        <input name="path" placeholder="ファイルシステム上のパス">
        <input name="max" value="1000">
        <input type="SUBMIT">
    </form>
    </body></html>""", "UTF-8"))
