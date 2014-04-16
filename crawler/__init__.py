__author__ = 'Takashi SASAKI'
import http.server
import sqlite3
#import cgi
import urllib.parse
import logging
import os


def do_POST(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    body_len = int(self.headers['Content-Length'])
    body_bytes = self.rfile.read(body_len)
    body_string = body_bytes.decode("ASCII")
    body_decoded = urllib.parse.unquote(body_string, "UTF-8")
    body_query = urllib.parse.parse_qs(body_decoded)

    path = body_query.get("path")[0]
    max = body_query.get("max")[0]
    max = int(max)
    logging.info(path)
    self.send_response(200)
    self.send_header("Content-Type", "text/plain; charset=UTF-8")
    self.end_headers()

    count = 0
    for dpath, dnames, fnames in os.walk(path):
        for x in dnames:
            self.wfile.write(bytes(x, "UTF-8"))
        count += 1
        if count == max: break
    self.wfile.write(bytes(path, "UTF-8"))


def do_GET(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.send_header("Content-Type", "text/html; charset=UTF-8")
    self.wfile.write(bytes("""<html><head><title></title></head><body>
    <form method="POST">
        <input name="path" placeholder="ファイルシステム上のパス">
        <input name="max" value="1000">
        <input type="SUBMIT">
    </form>
    </body></html>""", "UTF-8"))


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
