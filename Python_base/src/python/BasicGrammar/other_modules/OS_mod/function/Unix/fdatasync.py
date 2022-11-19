import os

"""
os.fdatasync(fd)：用于强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。如果你需要刷新缓冲区可以使用该方法。Unix上可用。
    fd -- 文件描述符
"""

# 打开文件
fd = os.open("/tmp/foo.txt", os.O_RDWR | os.O_CREAT)

# 写入字符串
os.write(fd, "This is test".encode('utf-8'))

os.fdatasync(fd)

# 读取文件
os.lseek(fd, 0, 0)
str1 = os.read(fd, 100)
print("读取的字符是 : ", str1)

# 关闭文件
os.close(fd)
