"""
上下文管理协议：即with语句，为了让一个对象兼容with语句，必须在这个对象的类中声明__enter__和__exit__方法。


__exit()：
    1.with语句中代码块出现异常，则with后的代码都无法执行
    2.返回值为True,那么异常会被清空，就好像啥都没发生一样，with后的语句正常执行。
"""


class Open:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('出现with语句，对象的__enter__被触发，有返回值则赋值给as声明的变量')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕时执行我啊')
        print(exc_type)  # 异常类型
        print(exc_val)  # 异常值
        print(exc_tb)  # 追溯信息
        return True


try:
    with Open('文件A') as f:
        print("f：{}".format(f.name))
        raise AttributeError('***AttributeError***')
except:
    pass
