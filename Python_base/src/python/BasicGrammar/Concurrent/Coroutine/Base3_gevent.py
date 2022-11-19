from gevent import monkey;monkey.patch_all() # 猴子补丁固定写法
import gevent
import time

print("---------------------- 遇到io主动切换 -------------------")


def eat(name):
    print('%s eat 1' % name)
    time.sleep(2)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    time.sleep(1)
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, name='egon')
gevent.joinall([g1, g2])
print('主线程结束')
