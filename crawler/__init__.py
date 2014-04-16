__author__ = 'Takashi SASAKI'
import http.server
import sqlite3


def do_POST(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.wfile.write(bytes("do_POST", "UTF-8"))
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
