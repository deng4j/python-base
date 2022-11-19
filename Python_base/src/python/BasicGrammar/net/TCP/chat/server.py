from socket import *
from multiprocessing import Process

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080))
server.listen(5)


def talk(conn, client_addr):
    while True:
        try:
            msg = conn.recv(1024)
            if not msg: break
            msg = "server 回复：" + msg.decode('utf-8')
            conn.send(msg.encode('utf-8'))
        except Exception:
            break


if __name__ == '__main__':
    while True:
        conn, client_addr = server.accept()
        p = Process(target=talk, args=(conn, client_addr))
        p.start()
        p.join()
