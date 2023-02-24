import os

"""
os.close(fd)：用于关闭指定的文件描述符 fd。
    fd -- 文件描述符。
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
fd = os.open(path, os.O_RDWR | os.O_CREAT)

#  写入字符串
os.write(fd, "This is test".encode("utf-8"))

# 关闭文件
os.close(fd)
