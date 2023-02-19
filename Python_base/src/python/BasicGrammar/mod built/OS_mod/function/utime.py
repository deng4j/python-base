import os

"""
os.utime(path, times)：用于设置指定路径文件最后的修改和访问时间。在Unix，Windows中有效。
    path -- 文件路径
    times -- 如果时间是 None, 则文件的访问和修改设为当前时间 。 否则, 时间是一个 2-tuple数字, (atime, mtime) 用来分别作为访问和修改的时间。
"""

path = 'D:\\window\\temp\\test.txt'

# 显示文件的 stat 信息
stinfo = os.stat(path)

print("test.txt 的访问时间: %s" % stinfo.st_atime)
print("test.txt 的修改时间: %s" % stinfo.st_mtime)

# 修改访问和修改时间
os.utime(path, (1330712280, 1330712292))
