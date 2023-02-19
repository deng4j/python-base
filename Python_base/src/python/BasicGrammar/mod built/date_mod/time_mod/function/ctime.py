from BasicGrammar.other_modules.date_mod.time_mod.function import time

"""
time.ctime([secs])：作用相当于asctime(localtime(secs))，未给参数相当于asctime()
"""

print("time.ctime() : %s" % time.ctime())
