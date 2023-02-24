import os

"""
os.path.islink(path)：判断路径是否为符号链接。windows直接返回false。

在Unix或Linux中，可以使用ln命令创建软链接或符号链接。下面是在shell提示符下创建符号链接的语法：
    $ ln -s {source-filename} {symbolic-filename}
"""

path = 'D:\\window\\temp\\test.txt'
path1 = "/home/ihritik/Desktop/file(shortcut).txt"

print(os.path.islink(path))
print(os.path.islink(path1))
