import os

"""
os.dup(fd)：用于复制文件描述符 fd。
    fd -- 文件描述符
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 复制文件描述符
d_fd = os.dup(fd)

# 写入字符串
os.write(d_fd, "This is test".encode('utf-8'))

# 关闭文件
os.closerange(fd, d_fd)
