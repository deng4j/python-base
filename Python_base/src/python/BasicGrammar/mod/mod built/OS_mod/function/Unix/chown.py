import os

"""
os.chown(path, uid, gid)：用于更改文件所有者，如果不修改可以设置为 -1, 你需要超级用户权限来执行权限修改操作。只支持在 Unix 下使用。
    path -- 设置权限的文件路径
    uid -- 所属用户 ID
    gid -- 所属用户组 ID
"""

path = "D:\\window\\temp\\test.txt"

# 设置所有者 ID 为 100
os.chown(path, 100, -1)
