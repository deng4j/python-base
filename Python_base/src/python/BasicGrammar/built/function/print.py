"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    *objects 可变参数，可以传入多个对象用于输出打印
    sep 多个对象输出在一行，中间使用sep进行分割
    end print函数在一次调用后输出打印以end结尾，默认是以\n结尾，因此一次print会输出一行数据
    file， 指定print会将*objects输出到哪里，默认输出到标准输出，也可以输出到文件中
    flush 如果为True，则不会进行缓存，而是强制刷新，如果为False，是否缓存取决于file参数传入的对象
"""

"""
print("\033[显示方式；前景颜色；背景颜色 m 字符串 \033[0m")

显示方式
    默认：     0
    高亮显示： 1
    下划线：   4
    闪烁：     5
    反白显示： 7
    不可见：   8


前景颜色和背景颜色,大于37将显示默认字体
    颜色      前景色     背景色

    黑色      30          40
    红色      31          41
    绿色      32          42
    黄色      33          43
    蓝色      34          44
    紫红色    35          45
    青蓝色    36          46
    白色      37          47
"""

print("-------------------------1-------------------------")

print('\033[0m这是显示方式0')
print('\033[1m这是显示方式1')
print('\033[4m这是显示方式4')
print('\033[5m这是显示方式5')
print('\033[7m这是显示方式7')
print('\033[8m这是显示方式8')
print('\033[30m这是前景色0')
print('\033[31m这是前景色1')
print('\033[32m这是前景色2')
print('\033[33m这是前景色3')
print('\033[34m这是前景色4')
print('\033[35m这是前景色5')
print('\033[36m这是前景色6')
print('\033[37m这是前景色7')
print('\033[40m这是背景色0')
print('\033[41m这是背景色1')
print('\033[42m这是背景色2')
print('\033[43m这是背景色3')
print('\033[44m这是背景色4')
print('\033[45m这是背景色5')
print('\033[46m这是背景色6')
print('\033[47m这是背景色7')

print("------------------------2--------------------------")

print("\033[31m 这是红色字体 \033[0m")
print("\033[32m 这是绿色字体 \033[0m")
print("\033[33m 这是黄色字体 \033[0m")
print("\033[34m 这是蓝色字体 \033[0m")
print("\033[38m 这是默认字体 \033[0m")
print("--------------------------------------------------")
print("\033[40m 这是白色背景 \033[0m")
print("\033[41m 这是红色背景 \033[0m")
print("\033[42m 这是绿色背景 \033[0m")
print("\033[43m 这是黄色背景 \033[0m")
print("\033[44m 这是蓝色背景 \033[0m")

print("-----------------------3---------------------------")

print("\033[1;31m  我  \033[0m")
print("\033[1;32m  我  \033[0m")
print("\033[1;33m  我  \033[0m")
print("\033[1;34m  我  \033[0m")
print("\033[1;38m  我  \033[0m")

print("-----------------------4---------------------------")

print("\033[0;37;41m  我  \033[0m")
print("\033[0;37;42m  我  \033[0m")
print("\033[0;37;43m  我  \033[0m")
print("\033[0;37;44m  我  \033[0m")
print("\033[0;37;45m  我  \033[0m")
print("\033[0;37;46m  我  \033[0m")
print("\033[0;30;47m  我  \033[0m")

print("------------------------关键字--------------------------")

print(2, 3, 4, sep=',')

print("你", end="|")
print("好", end="|")

print("\n------------------------输出到文件--------------------------")


def wToFile():
    from src.python.tools.GetRootFolder import getRelativePathsByRepositoryRoot
    paths = getRelativePathsByRepositoryRoot('Python_base',
                                             'Python_base/src/resources/file/folder1/print.txt')
    print(paths)
    f = open(paths, 'w')
    print("挥洒的汗水才是青春的光辉！！！！！！\n", file=f)
    f.close()
