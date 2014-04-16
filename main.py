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


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    __slot__ = ["pathList", "parsedUrl", "parsedQuery"]

    def __init__(self, request, client_address, server):
        logging.info(request)
        http.server.BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_POST(self):
        self.do_GET(post=True)

    def do_GET(self, post=False):
        self.pathList = self.path.split('/')[1:]
        if self.pathList[-1] == "":
            # ignoring last slash
            self.pathList = self.pathList[:-1]
        self.parsedUrl = urllib.parse.urlparse(self.path)
        self.parsedQuery = cgi.parse_qs(self.parsedUrl.query)
        logging.info(self.pathList)
        logging.info(self.parsedUrl)
        logging.info(self.parsedQuery)

        if (len(self.pathList) == 0):
            self.responseIndexHtml()
            return
        if (self.pathList[0] == ""):
            self.responseIndexHtml()
            return

        try:
            if (len(self.pathList) == 1):
                module = __import__(self.pathList[0], globals=globals(), locals=locals())
                if post == True:
                    module.do_POST(self)
                    return
                else:
                    module.do_GET(self)
                    return
        except ImportError as e:
            http.server.SimpleHTTPRequestHandler.do_GET(self)
            return
        except ValueError as e:
            http.server.SimpleHTTPRequestHandler.do_GET(self)
            return


        #data = {"server_id": "2T6CnTUUcqkY"}
        data = self.parsedQuery
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

    def responseIndexHtml(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        file = open("html/index.html", encoding='utf-8')
        body = file.read()
        self.wfile.write(bytes(body, "UTF-8"))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("IsUserAnAdmin = %s" % ctypes.windll.shell32.IsUserAnAdmin())
    httpd = MyHttpServer(("127.0.0.1", 80), MyHttpRequestHandler)
    httpd.serve_forever()
