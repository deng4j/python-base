import os

"""
os.fstat(fd)：返回文件描述符fd的状态，类似 stat()。
    fstat 方法返回的结构:
        st_dev: 设备信息
        st_ino: 文件的i-node值
        st_mode: 文件信息的掩码，包含了文件的权限信息，文件的类型信息(是普通文件还是管道文件，或者是其他的文件类型)
        st_nlink: 硬连接数
        st_uid: 用户ID
        st_gid: 用户组 ID
        st_rdev: 设备 ID (如果指定文件)
        st_size: 文件大小，以byte为单位
        st_blksize: 系统 I/O 块大小
        st_blocks: 文件的是由多少个 512 byte 的块构成的
        st_atime: 文件最近的访问时间
        st_mtime: 文件最近的修改时间
        st_ctime: 文件状态信息的修改时间（不是文件内容的修改时间）
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 获取元组
info = os.fstat(fd)

print("文件信息 :", info)

# 获取文件 uid
print("文件 UID :%d" % info.st_uid)

# 获取文件 gid
print("文件 GID  :%d" % info.st_gid)

# 关闭文件
os.close(fd)
