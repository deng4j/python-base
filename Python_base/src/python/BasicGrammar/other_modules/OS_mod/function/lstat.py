import os

"""
os.lstat(path)：用于类似 stat() 返回文件的信息,但是没有符号链接。在某些平台上，这是fstat的别名，例如 Windows。
"""

path = 'D:\\window\\temp\\test.txt'

fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 关闭打开的文件
os.close(fd)

# 获取元组
info = os.lstat(path)

print("文件信息 :", info)

# 获取文件 uid
print("文件 UID  :%d" % info.st_uid)

# 获取文件 gid
print("文件 GID :%d" % info.st_gid)
