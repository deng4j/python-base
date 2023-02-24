import os

"""
os.write(fd, str)：用于写入字符串到文件描述符 fd 中. 返回实际写入的字符串长度。
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
fd = os.open(path, os.O_RDWR | os.O_CREAT)

#  写入字符串
ret = os.write(fd, "This is test".encode("utf-8"))

print("写入的位数为: ", ret)

# 关闭文件
os.close(fd)
