import os

"""
os.lseek(fd, pos, how)：用于设置文件描述符 fd 当前位置为 pos, how 方式修改。在Unix，Windows中有效。
    fd -- 文件描述符。
    pos -- 这是相对于给定的参数 how 在文件中的位置。
    how -- 文件内参考位置。SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始。
"""

path = 'D:\\window\\temp\\test.txt'

fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 写入字符串
os.write(fd, "This is test".encode("utf-8"))

os.fsync(fd)

# 从开始位置读取字符串
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is : ", str)

# 关闭文件
os.close(fd)
