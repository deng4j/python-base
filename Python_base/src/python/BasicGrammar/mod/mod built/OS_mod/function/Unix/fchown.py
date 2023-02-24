import os

"""
os.fchown(fd, uid, gid)：用于修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。Unix上可用。
    fd -- 文件描述符
    uid -- 文件所有者的用户id
    gid -- 文件所有者的用户组id
"""

# 打开文件
fd = os.open("/tmp/foo.txt", os.O_RDONLY)

# 设置文件的用户 id 为 100
os.fchown(fd, 100, -1)

# 设置文件的用户组 id 为 50
os.fchown(fd, -1, 50)

print("修改权限成功!!")

# 关闭文件
os.close(fd)
