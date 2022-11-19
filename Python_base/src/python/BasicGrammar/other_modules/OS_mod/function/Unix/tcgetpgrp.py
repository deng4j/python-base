import os

"""
os.tcgetpgrp(fd)：用于回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组。
"""

path = 'D:\\window\\temp\\test.txt'

# 显示当前目录
print("当前目录 :%s" % os.getcwd())

fd = os.open(path, os.O_RDONLY)

f = os.tcgetpgrp(fd)

# 显示进程组
print("相关进程组: ", f)

os.close(fd)
