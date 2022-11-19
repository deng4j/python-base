import os

"""
os.closerange(fd_low, fd_high)：用于关闭所有文件描述符 fd，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略。
    fd_low -- 最小文件描述符
    fd_high -- 最大文件描述符
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 写入字符串
os.write(fd, "This is test".encode('utf-8'))

# 关闭文件
os.closerange(fd, fd)
