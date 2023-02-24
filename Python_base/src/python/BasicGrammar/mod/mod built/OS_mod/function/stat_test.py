import os

"""
os.stat(path):用于在给定的路径上执行一个系统 stat 的调用。

    stat 结构:
        st_mode: inode 保护模式
        st_ino: inode 节点号。
        st_dev: inode 驻留的设备。
        st_nlink: inode 的链接数。
        st_uid: 所有者的用户ID。
        st_gid: 所有者的组ID。
        st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
        st_atime: 上次访问的时间。
        st_mtime: 最后一次修改的时间。
        st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
"""

path = 'D:\\window\\temp\\test.txt'

statinfo = os.stat(path)

print(statinfo)
