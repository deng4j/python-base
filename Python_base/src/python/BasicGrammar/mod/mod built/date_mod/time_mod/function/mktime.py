from BasicGrammar.other_modules.date_mod.time_mod.function import time

"""
mktime() 函数执行与gmtime(), localtime()相反的操作，它接收struct_time对象作为参数，返回用秒数来表示时间的浮点数。
"""

now_time = time.localtime()  # 结构化时间

# 把结构化时间转换为时间戳格式
print(time.mktime(now_time))
