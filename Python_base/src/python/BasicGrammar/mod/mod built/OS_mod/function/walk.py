import os

"""
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])：在Unix，Windows中有效。
    1.可以创建一个生成器，用以生成所要查找的目录及其子目录下的所有文件。
    2.用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
    3.是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。
    
        top -- 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
        topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。
            如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
        onerror -- 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。
        followlinks -- 设置为 true，则通过软链接访问目录。
"""

path = 'D:\\window\\temp\\'

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
