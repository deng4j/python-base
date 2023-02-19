import os

"""
os.ftruncate(fd, length)：裁剪文件描述符fd对应的文件, 它最大不能超过文件大小。Unix上可用。
    fd -- 文件的描述符。
    length -- 要裁剪文件大小。
"""

# 打开文件
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# 写入字符串
os.write(fd, "This is test - This is test")

# 使用 ftruncate() 方法
os.ftruncate(fd, 10)

# 读取内容
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("读取的字符串是 : ", str)

# 关闭文件
os.close(fd)
