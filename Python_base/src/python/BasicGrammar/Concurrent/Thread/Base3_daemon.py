from threading import Thread
import time

"""
守护线程：守护线程会等待主线程运行完毕后被销毁。需要强调的是：运行完毕并非终止运行。
    1.对主进程来说，运行完毕指的是主进程代码运行完毕
    2.对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程统统运行完毕，主线程才算运行完毕
"""


def sing(name):
    time.sleep(1)
    print('唱歌：', name)


if __name__ == '__main__':
    t1 = Thread(target=sing, args=('一路向北',))
    t1.setDaemon(True)
    t1.start()

    t2 = Thread(target=sing, args=('青花瓷',), daemon=True)
    t2.start()

    # 测试主线程是否等待守护线程
    # time.sleep(4)
