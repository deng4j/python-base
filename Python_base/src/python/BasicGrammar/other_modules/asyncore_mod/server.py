import asyncore


# dispatcher的一个子类dispatcher_with_send
class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        if data:
            print(data.decode('utf-8'))
            self.send(data)


class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)  # 侦听与套接字的连接。

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        handler = EchoHandler(sock)


if __name__ == '__main__':
    server = EchoServer('localhost', 8080)
    asyncore.loop()
