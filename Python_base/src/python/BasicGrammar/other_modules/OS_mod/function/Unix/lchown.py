import os

"""
os.lchown(path, uid, gid)：用于更改文件所有者，类似 chown，但是不追踪链接。只支持在 Unix 下使用。
    path -- 设置权限的文件路径
    uid -- 所属用户 ID
    gid -- 所属用户组 ID 
"""

# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 关闭打开的文件
os.close(fd)

# 修改文件权限，设置文件所属用户 ID
os.lchown(path, 500, -1)

# 设置文件所属用户组 ID
os.lchown(path, -1, 500)
