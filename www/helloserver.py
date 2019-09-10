#!/usr/local/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(
			'<h1>Welcome</h1><p>Hello from Python!</p>')
		return
        except IOError:
		self.send_error(500,'Unexpected I/O Error')

def main():
    try:
        server = HTTPServer(('', 8080), MyHandler)
        print('started httpserver...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Interrupted, so goodbye!')
        server.socket.close()

if __name__ == '__main__':
    main()

