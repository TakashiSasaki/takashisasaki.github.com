__author__ = 'Takashi SASAKI'
import http.server
import ctypes
import logging
import json
import urllib.parse
import cgi


class MyHttpServer(http.server.HTTPServer):
    def __init__(self, server_address, handler_class):
        http.server.HTTPServer.__init__(self, server_address, handler_class)


class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    __slot__ = ["pathList", "parsedUrl", "parsedQuery"]

    def __init__(self, request, client_address, server):
        logging.info(request)
        http.server.BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_GET(self):
        self.pathList = self.path.split('/')[1:]
        self.parsedUrl = urllib.parse.urlparse(self.path)
        self.parsedQuery = cgi.parse_qs(self.parsedUrl.query)
        logging.info(self.pathList)
        logging.info(self.parsedUrl)
        logging.info(self.parsedQuery)

        try:
            if (len(self.pathList) == 1):
                module = __import__(self.pathList[0], globals=globals(), locals=locals())
                module.do_GET(self)
                return
        except ImportError as e:
            pass
        except ValueError as e:
            pass

        data = {"server_id": "2T6CnTUUcqkY"}
        if self.parsedQuery.get("callback") is not None:
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript")
            self.end_headers()
            callback = self.parsedQuery["callback"][0]
            self.wfile.write(bytes(callback + "(" + json.dumps(data) + ");", "UTF-8"))
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(data), "UTF-8"))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("IsUserAnAdmin = %s" % ctypes.windll.shell32.IsUserAnAdmin())
    httpd = MyHttpServer(("127.0.0.1", 8000), MyHttpRequestHandler)
    httpd.serve_forever()
