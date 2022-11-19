import os

"""
os.ttyname(fd)：用于返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
"""

path = 'D:\\window\\temp\\test.txt'

# 显示当前目录
print("当前目录 :%s" % os.getcwd())

fd = os.open(path, os.O_RDONLY)

p = os.ttyname(fd)

print("关联的终端为: ", p)

os.close(fd)
