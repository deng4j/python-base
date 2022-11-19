import os

"""
os.dup2(fd, fd2)：用于将一个文件描述符 fd 复制到另一个 fd2。Unix, Windows 上可用。
    fd -- 要被复制的文件描述符
    fd2 -- 复制的文件描述符
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
f = open(path, 'a')

# 将这个文件描述符代表的文件，传递给 1 描述符指向的文件（也就是 stdout）
os.dup2(f.fileno(), 1)

# 关闭文件
f.close()

# print 输出到标准输出流，就是文件描述符1
print('runoob')
print('google')
