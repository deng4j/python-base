from BasicGrammar.other_modules.date_mod.time_mod.function import time

"""
time.sleep(secs)：推迟调用线程的运行，secs指秒数。
"""

print("Start : %s" % time.ctime())
time.sleep(3)
print("End : %s" % time.ctime())
