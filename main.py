from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = 'localhost'
port_num = 8080


class MyServer(BaseHTTPRequestHandler):
    """Based"""
    def do_POST(self):
        """POST-запрос"""
        content_len = int(self.headers.get('Content-Length'))
        content_data = self.rfile.read(content_len)

        print(content_data.decode())

    def do_GET(self):
        """GET-запрос"""
        self.send_response(200)

        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(bytes("Hello, World wide web!", 'utf-8'))


if __name__ == '__main__':
    server = HTTPServer((host_name, port_num), MyServer)
    print('http://%s:%s' % (host_name, port_num))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print('Сервер наконец закрыт, спасибо')
