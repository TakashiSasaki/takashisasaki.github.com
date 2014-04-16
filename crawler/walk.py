import http
import os
import logging
import urllib.parse
import threading
import sqlite3


class WalkTable(object):
    def __init__(self):
        self.connection = sqlite3.connect("crawler.sqlite")
        try:
            self.create()
        except sqlite3.OperationalError as e:
            pass

    def create(self):
        self.connection.execute("""CREATE TABLE walk
                                  (path TEXT(1000), last_visited INTEGER, last_read INTEGER,
                                  size INTEGER, last_modified INTEGER, created INTEGER, last_accessed);""")

    def insert(self, path, last_visited=None, last_read=None, size=None, last_modified=None, created=None,
               last_accessed=None):
        self.connection.execute("INSERT INTO walk VALUES (?,?,?,?,?,?,?)",
                                (path, last_visited, last_read, size, last_modified, created, last_accessed))


class WalkThread(threading.Thread):
    thread = None

    @classmethod
    def isAlive(cls):
        if cls.thread is not None:
            isinstance(cls.thread, threading.Thread)
            return threading.Thread.isAlive(cls.thread)
        return False

    @classmethod
    def getCount(cls):
        if cls.thread is not None:
            return cls.thread.count
        return 0

    def __init__(self, path, max):
        threading.Thread.__init__(self)
        if self.isAlive():
            raise Exception("WalkThread is already running")
        WalkThread.thread = self
        self.path = path
        self.max = max

    def run(self):
        walk_table = WalkTable()
        self.count = 0
        for dpath, dnames, fnames in os.walk(self.path):
            for dname in dnames:
                walk_table.insert(dpath + os.path.sep + dname)
            for fname in fnames:
                walk_table.insert(dpath + os.path.sep + fname)
            self.count += 1
            if self.count == max: break


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

    walk_thread = WalkThread(path, max)
    walk_thread.start()
    self.wfile.write(bytes(path, "UTF-8"))


def do_GET(self):
    assert isinstance(self, http.server.BaseHTTPRequestHandler)
    self.send_response(200)
    self.send_header("Content-Type", "text/plain; charset=UTF-8")
    self.end_headers()

    if WalkThread.thread:
        self.wfile.write(bytes("WalkThread is running\n", "UTF-8"))
    else:
        self.wfile.write(bytes("WalkThread is not running\n", "UTF-8"))

    self.wfile.write(bytes("count = %s\n" % WalkThread.getCount(), "UTF-8"))