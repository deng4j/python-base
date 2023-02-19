import glob

"""
glob模块用来查找文件目录和文件，并将搜索的到的结果返回到一个列表中，

常见的两个方法有glob.glob()和glob.iglob()，可以和常用的find功能进行类比，glob支持*、?、[]这三种通配符。
 - *代表0个或多个字符
 - ?代表一个字符
 - []匹配指定范围内的字符，如[0-9]匹配数字
"""


def m1():
    # 搜索".jpg"格式的文件
    f = glob.glob(r'./files/*.jpg')
    print(f)


def m2():
    # 搜索".jpg"格式的文件
    f = glob.iglob(r'./files/*.jpg')
    print(f)
    for i in f:
        print(i)


if __name__ == "__main__":
    m1()
    m2()
