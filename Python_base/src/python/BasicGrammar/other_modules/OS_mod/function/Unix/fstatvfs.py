import os

"""
os.fstatvfs(fd)：用于返回包含文件描述符fd的文件的文件系统的信息，Python 3.3 相等于 statvfs()。Unix上可用。
    fstatvfs 方法返回的结构:
        f_bsize: 文件系统块大小
        f_frsize: 分栈大小
        f_blocks: 文件系统数据块总数
        f_bfree: 可用块数
        f_bavail:非超级用户可获取的块数
        f_files: 文件结点总数
        f_ffree: 可用文件结点数
        f_favail: 非超级用户的可用文件结点数
        f_fsid: 文件系统标识 ID
        f_flag: 挂载标记
        f_namemax: 最大文件长度
"""

# 打开文件
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# 获取元组
info = os.fstatvfs(fd)

print("文件信息 :", info)

# 获取文件名最大长度
print("文件名最大长度 :%d" % info.f_namemax)

# 获取可用块数
print("可用块数 :%d" % info.f_bfree)

# 关闭文件
os.close(fd)
