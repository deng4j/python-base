import asyncore
import sys

"""
相比python原生的socket api，asyncore具备有很大的优势，asyncore对原生的socket进行封装，提供非常简洁优秀的接口，
    利用asyncore覆写相关需要处理的接口方法，就可以完成一个socket的网络编程，从而不需要处理复杂的socket网络状况以及多线程处理等等。


writable 回调函数
    描述是否有数据需要被发送到服务器。返回值为 `True` 表示可写，`False` 表示不可写，
    如果不实现默认返回为 `True`，当返回 `True` 时，回调函数 `handle_write` 将被触发。

handle_write()
    当异步循环检测到一个可写套接字可以被写入时会被调用。 通常此方法将实现必要的缓冲机制以保证运行效率。

`readable` 回调函数
    描述是否有数据从服务端读取。返回 `True` 表示有数据需要读取，`False` 表示没有数据需要被读取，当不实现默认返回为 `True`，
    当返回 `True` 时，回调函数 `handle_read` 将被触发。

`handle_read` 回调函数
    当有数据需要读取时触发（`readable` 回调函数返回 `True` 时），该函数被触发，通常情况下在该函数中编写 `recv` 方法接收数据。
"""


# 1. 定义类并且继承自 asyncore.dispatcher
class SocketClient(asyncore.dispatcher):
    # 2. 实现类中的回调函数代码
    def __init__(self, host, port):
        self.msg = '你好！'
        # 调用父类方法
        asyncore.dispatcher.__init__(self)

        # 创建 Socket 对象
        self.create_socket()

        # 连接服务器
        address = (host, port)
        self.connect(address)
        pass

    # 实现 handle_connect 回调函数，当 `Socket` 连接服务器成功时回调该函数
    def handle_connect(self):
        print("连接成功")

    # 实现 `handle_write` 回调函数
    def writable(self):
        print("writable 回调函")
        return True

    # 实现 handle_write 回调函数
    def handle_write(self):
        # 内部实现对服务器发送数据的代码
        # 调用 send 方法发送数据，参数是字节数据
        self.send(self.msg.encode('utf-8'))

    # 实现 readable 回调函数
    def readable(self):
        return True

    # 实现 handle_read 回调函数
    def handle_read(self):
        # 主动接收数据，参数是需要接收数据的长度
        result = self.recv(1024)
        print(result.decode('utf-8'))

    # 实现 handle_error 回调函数
    def handle_error(self):
        # 编写处理错误方法
        t, e, trace = sys.exc_info()
        self.close()

    # 实现 handle_close 回调函数
    def handle_close(self):
        print("连接关闭")
        self.close()


# 3. 创建对象并且执行 asyncore.loop 进入运行循环

if __name__ == '__main__':
    client = SocketClient('127.0.0.1', 8080)
    client.msg = 'hello world！！！'
    # 开始启动运行循环
    asyncore.loop(timeout=0.001)
