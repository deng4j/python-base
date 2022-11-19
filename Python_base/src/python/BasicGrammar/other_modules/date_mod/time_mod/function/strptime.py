from BasicGrammar.other_modules.date_mod.time_mod.function import time

"""
time.strptime(str,fmt='%a %b %d %H:%M:%S %Y'):根据fmt的格式把一个时间字符串解析为时间元组。
"""

struct_time = time.strptime("30 Nov 00", "%d %b %y")
print("返回元组: ", struct_time)
