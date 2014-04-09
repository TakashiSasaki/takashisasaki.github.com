__author__ = 'sasaki'
import logging
#import http.server
import main


def do_GET(self):
    assert isinstance(self, main.MyHttpRequestHandler)
    logging.info("handler1.py")
    self.send_response(200)
    self.send_header("Content-Type", "text/plain")
    self.end_headers()
    self.wfile.write(bytes("handler1.py", "UTF-8"))