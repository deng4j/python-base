from BasicGrammar.other_modules.date_mod.time_mod.function import time

"""
time.perf_counter()返回计时器的精准时间（系统的运行时间），包含整个系统的睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。
"""

a = time.perf_counter()  # 第一次调用per_counter,所以a值应该为零,但是他不是刚好为零
print(a)

time.sleep(5)

b = time.perf_counter()  # sleep5秒后,b的值就应该是5
print(b)
