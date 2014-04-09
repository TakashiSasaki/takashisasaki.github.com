__author__ = 'Takashi SASAKI'
import http.server
import ctypes
import logging


class MyHttpServer(http.server.HTTPServer):
    def __init__(self, server_address, handler_class):
        http.server.HTTPServer.__init__(self, server_address, handler_class)


class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        logging.info(request)
        http.server.BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("hello", "UTF-8"))
        #self.wfile.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("IsUserAnAdmin = %s" % ctypes.windll.shell32.IsUserAnAdmin())
    httpd = MyHttpServer(("127.0.0.1", 8000), MyHttpRequestHandler)
    httpd.serve_forever()
