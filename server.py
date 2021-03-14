import http.server
import socketserver

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Run server at 127.0.0.1:{}".format(PORT))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('catched!')

