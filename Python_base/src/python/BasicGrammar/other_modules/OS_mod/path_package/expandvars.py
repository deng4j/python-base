import os

"""
os.path.expandvars(path):根据环境变量的值替换path中包含的"$name"和"${name}"
"""

path1 = R"%HOMEPATH%\Directory\file.txt"
path2 = R"C:\Users\$USERNAME\Directory\file.txt"
path3 = R"${TEMP}\file.txt"

print(os.path.expandvars(path1))
print(os.path.expandvars(path2))
print(os.path.expandvars(path3))
