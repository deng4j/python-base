import sys

sys.path.append("..")  # 告诉解释器模块的路径

import Module1, Module2

Module1.module1()
Module2.module2()

for i in sys.argv:
    print(i)

print(' python 路径为', sys.path)
