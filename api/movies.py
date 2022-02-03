from email import message
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_Get(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = 'this works'
        self.wfile.write(message.encode())