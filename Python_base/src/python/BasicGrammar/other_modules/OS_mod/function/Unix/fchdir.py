import os

"""
os.fchdir(fd)：通过文件描述符改变当前工作目录。Unix 上可用。
    fd -- 文件描述符。
"""

# 首先到目录
os.chdir("/var/www/html")

print("当前目录：{}".format(os.getcwd()))

# 打开新目录
fd = os.open("/tmp", os.O_RDONLY)

# 使用 os.fchdir() 方法修改到新目录
os.fchdir(fd)

print("当前目录：{}".format(os.getcwd()))

# 关闭打开的目录
os.close(fd)
