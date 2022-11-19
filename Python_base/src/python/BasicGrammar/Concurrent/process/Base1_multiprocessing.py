import multiprocessing
import time

"""
主进程会等待全部子进程执行结束再结束

multiprocessing.Process([group [, target [, name [, args [, kwargs]]]]])
    参数：
        group参数未使用，值始终为None
        target表示调用对象，即子进程要执行的任务
        args表示调用对象的位置参数元组，args=(1,2,'egon',)
        kwargs表示调用对象的字典，kwargs={'name':'egon','age':18}
        name为子进程的名称
    方法:
        p.start()：启动进程，并调用该子进程中的p.run()。
        p.run()：进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法。
        p.terminate()：强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，
            使用该方法需要特别小心这种情况。如果p还保存了一个锁那么也将不会被释放，进而导致死锁。
        p.is_alive()：如果p仍然运行，返回True
        p.join([timeout])：主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。
            timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程。
            
     属性介绍：
            p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，
                并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置
            p.name：进程的名称
            p.pid：进程的pid
            p.exitcode：进程在运行时为None、如果为–N，表示被信号N结束(了解即可)
            p.authkey：进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。这个键的用途是为涉及网络连接
                的底层进程间通信提供安全性，这类连接只有在具有相同的身份验证键时才能成功（了解即可）
"""


def sing(str):
    for i in range(3):
        print("唱歌：", str)
        time.sleep(1)


def dance(str):
    for i in range(3):
        print("跳舞：", str)
        time.sleep(0.5)


if __name__ == '__main__':
    multiprocessing.freeze_support()

    # 1.使用进程类创建进程对象
    # target指定执行进程的函数名
    sing_process = multiprocessing.Process(target=sing, args=('一路向北',))
    dance_process = multiprocessing.Process(target=dance, kwargs={'str': '姬霓太美'})

    # 使用进程对象启动进程任务
    sing_process.start()
    dance_process.start()

    # 等待进程结束
    sing_process.join()
    dance_process.join()

    print(sing_process.pid)
    print(dance_process.pid)
