import os

"""
os.tcsetpgrp(fd, pg)：用于设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。可用系统: Unix。
    fd -- 文件描述符。
    pg -- 关联的进程组。
"""

path = 'D:\\window\\temp\\test.txt'

# 显示当前目录
print("当前目录 :%s" % os.getcwd())

fd = os.open(path, os.O_RDONLY)

f = os.tcgetpgrp(fd)

# 显示进程组
print("相关进程组: ", f)

# 设置进程组
os.tcsetpgrp(fd, 2672)

os.close(fd)
