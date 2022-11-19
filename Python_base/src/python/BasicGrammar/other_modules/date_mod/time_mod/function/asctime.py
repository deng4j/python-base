from BasicGrammar.other_modules.date_mod.time_mod.function import time

"""
time.asctime([tupletime])接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
"""

print("time.asctime(time.localtime()): %s " % time.asctime(time.localtime()))
