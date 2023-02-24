import os

"""
os.stat_float_times([newvalue]):用于决定stat_result是否以float对象显示时间戳。
    newvalue -- 如果为 True, 调用 stat() 返回 floats,如果 False, 调用 stat 返回 ints。如果没有该参数返回当前设置。
"""

path = 'D:\\window\\temp\\test.txt'

statinfo = os.stat(path)

print(statinfo)

statinfo = os.stat_float_times()
print(statinfo)
