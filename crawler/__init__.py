__author__ = 'Takashi SASAKI'
import http.server
import sqlite3
import cgi
import logging


def do_POST(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    body_len = int(self.headers['Content-Length'])
    body = self.rfile.read(body_len)
    decoded_body = cgi.parse_qs(body)
    path_bytes = decoded_body.get(b"path")[0]
    path_utf8 = path_bytes.decode("UTF-8")
    logging.info(path_utf8)
    self.wfile.write(bytes(path_utf8, "UTF-8"))
    pass


def do_GET(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.wfile.write(bytes("""<html><head><title></title></head><body>
    <form method="POST">
        <input name="path" placeholder="ファイルシステム上のパス">
        <input type="SUBMIT">
    </form>
    </body></html>""", "UTF-8"))
    pass


class CrawlerTable(object):
    def __init__(self):
        pass

    def createTable(self):
        self.connection = sqlite3.connect("crawler.sqlite")
        self.connection.execute("""CREATE TABLE log
                                  (path TEXT(1000), last_visited INTEGER, last_read INTEGER,
                                  size INTEGER, last_modified INTEGER, created INTEGER, last_accessed);""")

    def insertLog(self, path, last_visited, last_read, size, last_modified, created, last_accessed):
        self.connection.execute("INSERT INTO log VALUES (?,?,?,?,?,?,?)",
                                (path, last_visited, last_read, size, last_modified, created, last_accessed))
