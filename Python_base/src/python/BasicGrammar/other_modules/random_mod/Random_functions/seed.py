import random

"""
seed(x) 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。
    x -- 改变随机数生成器的种子seed。
"""

random.seed()

print("使用默认种子生成随机数：", random.random())

random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())

random.seed("hello", 2)
print("使用字符串种子生成随机数：", random.random())
