import os

"""
os.fsync(fd)：强制将文件描述符为fd的文件写入硬盘。在Unix, 将调用fsync()函数;在Windows, 调用 _commit()函数。

如果你准备操作一个Python文件对象f, 首先f.flush(),然后os.fsync(f.fileno()),
 确保与f相关的所有内存都写入了硬盘.在unix，Windows中有效。
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
fd = os.open(path, os.O_RDWR | os.O_CREAT)

#  写入字符串
os.write(fd, "This is test".encode("utf-8"))

# 使用 fsync() 方法.
os.fsync(fd)

# 读取内容
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("读取的字符串为 : ", str)

# 关闭文件
os.close(fd)
