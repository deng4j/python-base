import os

"""
os.popen(command[, mode[, bufsize]])： 方法用于从一个命令打开一个管道。在Unix，Windows中有效。
    command -- 使用的命令。
    mode -- 模式权限可以是 'r'(默认) 或 'w'。
    bufsize -- 指明了文件需要的缓冲大小：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲（大概值，以字节为单位）。
        负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。
        如果没有改参数，使用系统的默认值。
"""

# 使用 mkdir 命令
a = 'mkdir D:\\window\\temp\\test\\testPopen'

b = os.popen(a, 'r', 1)

print(b)
