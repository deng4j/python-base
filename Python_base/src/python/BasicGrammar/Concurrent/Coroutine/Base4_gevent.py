from gevent import monkey;monkey.patch_all()
import gevent

print("---------------------- 遇到io主动切换 -------------------")


def eat(name):
    print('%s eat 1' % name)
    gevent.sleep(2)  # time.sleep(2)或其他的阻塞，gevent是不能直接识别的需要用from gevent import monkey;monkey.patch_all()，放在第一行
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    gevent.sleep(1)
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, name='egon')
gevent.joinall([g1, g2])
print('主线程结束')
