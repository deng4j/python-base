from BasicGrammar.other_modules.date_mod.time_mod.function import time

"""
time.gmtime([secs])接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
"""

print("gmtime :", time.gmtime(1455508609.34375))
