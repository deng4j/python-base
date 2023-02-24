import os

"""
os.path.realpath(path):用于通过消除路径中遇到的任何符号链接来获取指定文件名的规范路径。

在shell提示符下创建符号链接的语法：$ ln -s {source-filename} {symbolic-filename}
"""

path = "/home / ihritik / Desktop / file(shortcut).txt"

print(os.path.realpath(path))
