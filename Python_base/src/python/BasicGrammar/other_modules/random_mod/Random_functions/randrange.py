import random

"""
randrange([start,] stop [,step]) 方法返回指定递增基数集合中的一个随机数，基数默认值为1。
    start -- 指定范围内的开始值，包含在范围内。
    stop -- 指定范围内的结束值，不包含在范围内。
    step -- 指定递增基数。
"""

# 从 1-100 中选取一个奇数
print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))

# 从 0-99 选取一个随机数
print("randrange(100) : ", random.randrange(100))
