import os

"""
os.read(fd,n) 方法用于从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，
    文件描述符 fd对应文件已达到结尾, 返回一个空字符串。在Unix，Windows中有效。
    
    fd -- 文件描述符。
    n -- 读取的字节。
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 读取文本
ret = os.read(fd, 12)
print(ret.decode('UTF-8'))

# 关闭文件
os.close(fd)
