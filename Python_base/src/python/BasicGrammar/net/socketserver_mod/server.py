import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        conn = self.request
        conn.sendall(b'welcome server')
        while True:
            data = conn.recv(1024)
            if data == b'close':
                print('cloed!!!')
                break
            print("recieve{}  from{}".format(data, self.client_address))
            conn.sendall(data)


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer)
    server.serve_forever()
