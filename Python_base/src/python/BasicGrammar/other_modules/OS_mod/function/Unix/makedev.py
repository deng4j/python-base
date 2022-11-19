import os

"""
os.makedev(major, minor):用于以major和minor设备号组成一个原始设备号。
    major -- Major 设备号。
    minor -- inor 设备号。
"""

path = 'D:\\window\\temp\\test.txt'

# 获取元组
info = os.lstat(path)

# 获取 major 和 minor 设备号
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print("Major 设备号 :", major_dnum)
print("Minor 设备号 :", minor_dnum)

# 生成设备号
dev_num = os.makedev(major_dnum, minor_dnum)
print("设备号 :", dev_num)
