from BasicGrammar.other_modules.date_mod.time_mod.function import time

"""
time.process_time()：返回当前进程执行 CPU 的时间总和，不包含睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。

process_time_ns()：与process_time()相似，它始终以纳秒为单位给出时间的整数值。
"""

start = time.process_time()

time.sleep(3)

for i in range(50):
    print(i, end=' ')

stop = time.process_time()

print('\n')
print("Elapsed time:{} {}".format(start, stop))
