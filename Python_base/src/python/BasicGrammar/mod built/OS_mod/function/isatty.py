import os

"""
os.isatty() 方法用于判断如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 使用 isatty() 查看文件
ret = os.isatty(fd)

print("返回值: ", ret)

# 关闭文件
os.close(fd)
