from threading import Thread
import time


# 多个线程抢占资源的情况

def work():
    global n
    strN = str(n) + "\n"
    print(strN)
    n -= 1
    time.sleep(0.2)


# 结果可能不为1
if __name__ == '__main__':
    n = 10
    lists = []
    for i in range(10):
        p = Thread(target=work)
        lists.append(p)
        p.start()
    for p in lists:
        p.join()
