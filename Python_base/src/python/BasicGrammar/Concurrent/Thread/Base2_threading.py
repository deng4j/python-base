from threading import Thread
import time


class sing(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(1)
        print("唱歌：", self.name)


if __name__ == '__main__':
    s1 = sing("月亮船")
    s2 = sing("北京东路的日子")
    s1.start()
    s2.start()
