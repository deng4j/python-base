import os, time
import random
from multiprocessing import Pool

"""

异步apply_async用法：如果使用异步提交的任务，主进程需要使用join，等待进程池内任务都处理完，
    然后可以用get收集结果。否则，主进程结束，进程池可能还没来得及执行，也就跟着一起结束了。
    

异步运行，根据进程池中有的进程数，每次最多3个子进程在异步执行。
返回结果之后，将结果放入列表，归还进程，之后再执行新的任务
需要注意的是，进程池中的三个进程不会同时开启或者同时结束
而是执行完一个就释放一个进程，这个进程就去接收新的任务。
"""


def work(n):
    print('%s run' % os.getpid())
    time.sleep(random.random())
    return n ** 2


# 同步
if __name__ == '__main__':
    p = Pool(3)
    res_l = []
    for i in range(5):
        # 同步调用，直到本次任务执行完毕拿到res，等待任务work执行的过程中可能有阻塞也可能没有阻塞
        res = p.apply_async(work, args=(i,))
        res_l.append(res)

    p.close()
    p.join()

    for res in res_l:
        print(res.get())
