from multiprocessing import Process, Pipe
import os

"""
Pipe([duplex])：返回一对 Connection 对象 (conn1, conn2) ， 分别表示管道的两端。
    如果 duplex 被置为 True (默认值)，那么该管道是双向的。如果 duplex 被置为 False ，那么该管道是单向的，即 conn1 只能用于接收消息，而 conn2 仅能用于发送消息。

Connection：
    send(obj)：将一个对象发送到连接的另一端，可以用 recv() 读取。
    recv()：返回一个由另一端使用 send() 发送的对象。该方法会一直阻塞直到接收到对象。 如果对端关闭了连接或者没有东西可接收，将抛出 EOFError 异常。
    fileno()返回由连接对象使用的描述符或者句柄。
    close()关闭连接对象。
    poll([timeout])返回连接对象中是否有可以读取的数据。如果未指定 timeout ，此方法会马上返回。如果 timeout 是一个数字，则指定了最大阻塞的秒数。如果 timeout 是 None，那么将一直等待，不会超时。
    send_bytes(buffer[, offset[, size]])：从一个 bytes-like object 对象中取出字节数组并作为一条完整消息发送。
    recv_bytes([maxlength])以字符串形式返回一条从连接对象另一端发送过来的字节数据。此方法在接收到数据前将一直阻塞。 如果连接对象被对端关闭或者没有数据可读取，将抛出 EOFError 异常。
    recv_bytes_into(buffer[, offset])将一条完整的字节数据消息读入 buffer 中并返回消息的字节数。 此方法在接收到数据前将一直阻塞。 如果连接对象被对端关闭或者没有数据可读取，将抛出 EOFError  异常。
"""


def f(conn):
    msg = 'pid:{} send:{}'.format(os.getpid(), '你好啊')
    conn.send(msg)
    print('pid:{} recv:[{}]'.format(os.getpid(), conn.recv()))
    conn.close()


if __name__ == "__main__":
    # 产生两个返回对象，一个是管道这一头，一个是另一头
    conn1, conn2 = Pipe()
    p1 = Process(target=f, args=(conn1,))
    p2 = Process(target=f, args=(conn2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
