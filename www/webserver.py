#!/usr/bin/env python

# Portions Copyright Jon Berg, turtlemeat.com

import string,cgi,time
from os import curdir, sep
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("doGet: path==" + self.path)
        try:
            if self.path == "/":
                self.path = "index.html"
                if self.path.endswith(".html"):
                    f = open(curdir + sep + self.path) #self.path has /test.html

                    # note that the above line potentially makes every file on your computer readable by the internet

                    self.send_response(200)
                    self.send_header('Content-type',    'text/html')
                    self.end_headers()
                    self.wfile.write(f.read())
                    f.close()
                    return
                if self.path.endswith(".esp"):   #our dynamic content
                    self.send_response(200)
                    self.send_header('Content-type',    'text/html')
                    self.end_headers()
                    self.wfile.write("hey, today is the " + str(time.localtime()[7]))
                    self.wfile.write(" day in the year " + str(time.localtime()[0]))
                    return
            return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)

            self.end_headers()
            upfilecontent = query.get('upfile')
            print("filecontent", upfilecontent[0])
            # Note that for this demo, for security, we don't actually save the file.
            self.wfile.write("<HTML>POST OK.<BR><BR>");
            self.wfile.write(upfilecontent[0]);

        except :
            pass

def main():
    try:
        server = HTTPServer(('', 6666), MyHandler)
        print('started httpserver...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()

if __name__ == '__main__':
    main()

