def print__name__():
    print("mod模块__name__：", __name__)


def exec():
    print("mod模块执行exec")


# 一般用作项目的主方法使用，也可以防止导入的模块执行函数
if __name__ == '__main__':
    exec()
