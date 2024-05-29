from http.server import SimpleHTTPRequestHandler, HTTPServer

class MediaHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def run(server_class=HTTPServer, handler_class=MediaHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting media server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()