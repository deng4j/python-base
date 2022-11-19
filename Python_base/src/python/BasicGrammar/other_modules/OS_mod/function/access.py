import os

"""
os.access(path, mode)：使用当前的uid/gid尝试访问路径。大部分操作使用有效的 uid/gid, 因此运行环境可以在 suid/sgid 环境尝试。如果允许访问返回 True , 否则返回False。
    path -- 要用来检测是否有访问权限的路径。
    mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
        os.F_OK: 作为access()的mode参数，测试path是否存在。
        os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
        os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
        os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
"""

# 查看path是否存在
have = os.access("D:\\window\\temp\\test.txt", os.F_OK)
print(have)

# 查看是否有读权限
r = os.access("D:\\window\\temp\\test.txt", os.R_OK)
print(r)

# 查看是否有写权限
w = os.access("D:\\window\\temp\\test.txt", os.W_OK)
print(w)

# 查看是否可执行
x = os.access("D:\\window\\temp\\test.txt", os.X_OK)
print(x)
