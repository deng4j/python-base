from BasicGrammar.other_modules.date_mod.time_mod.function import time

"""
time.localtime([secs])：接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
"""

print("localtime(): ", time.localtime(1455508609.34375))
