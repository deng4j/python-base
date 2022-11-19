"""
open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    file：表示将要打开的文件的路径（绝对路径或者相对当前工作目录的路径)
    mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
    buffering 是一个可选的整数，用于设置缓冲策略。 传入 0 来关闭缓冲（只允许在二进制模式下），传入 1 来选择行缓冲（只在文本模式下可用），传入一个整数 > 1 来表示固定大小的块缓冲区的字节大小。
    errors 是一个可选的字符串参数，用于指定如何处理编码和解码错误 - 这不能在二进制模式下使用。
    newline 指定换行符，默认是None，表示启用通用换行符。
    closefd 为 False 且给出的不是文件名而是文件描述符，那么当文件关闭时，底层文件描述符将保持打开状态。如果给出的是文件名，则 closefd 必须为 True （默认值），否则将触发错误。
    opener 来使用自定义开启器。然后通过使用参数（ file，flags ）调用 opener 获得文件对象的基础文件描述符。 opener 必须返回一个打开的文件描述符（使用 os.open as opener 时与传递 None 的效果相同）。

f.read(size)：返回一定数量的内容， size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。

f.readline()：会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
f.readlines()：返回该文件中包含的所有行。如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。

f.write(str_class)：将 str_class 写入到文件中, 然后返回写入的字符数。

f.writelines(lines):将一个由字符串组成的列表写入到文件。

f.flush():将缓冲区的数据刷入文件。

f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

f.seek()可以改变指针所在位置，f.seek(offset, from_what) ，from_what 值为默认为0，即文件开头。：
    seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符。
    seek(x,1) ： 表示从当前位置往后移动x个字符
    seek(-x,2)：表示从文件的结尾往前移动x个字符

r： 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
r+：打开一个文件用于读写。文件指针将会放在文件的开头。
w： 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+：打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a： 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+: 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
b:  以二进制格式操作

合法的mode有：
    r、rb、r+、rb+、w、wb、w+、wb+、a、ab、a+、ab+
-------------------------------------------------------------------------
模式          r       r+      w       w+      a       a+
读           √       √               √                √
写                   √       √       √       √        √
创建                         √       √       √        √
覆盖                         √       √
指针在开始    √       √       √       √
指针在末尾                                    √        √
"""

from src.python.tools.GetRootFolder import getRepositoryRootPath

root_paths = getRepositoryRootPath()

print("----------------------------- write --------------------------------")

f = open(root_paths + "Python_base/src/resources/file/folder1/textIO.txt", "w",
         encoding='utf-8')
num = f.write("一定有什么事是只有你才能做到的\n哈哈哈哈哈哈哈\n")
print(num)
f.close()

print("----------------------------- read --------------------------------")

# 打开一个文件
f = open(root_paths + "Python_base/src/resources/file/folder1/textIO.txt", "r",
         encoding='utf-8')
strAll = f.read()  # 返回整个文件内容
print(strAll)
f.close()  # 关闭文件

print("----------------------------- readline --------------------------------")

f = open(root_paths + "Python_base/src/resources/file/folder1/textIO.txt", "r",
         encoding='utf-8')
str = f.readline()
print(str)
f.close()

print("----------------------------- readlines --------------------------------")

f = open(root_paths + "Python_base/src/resources/file/folder1/textIO.txt", "r",
         encoding='utf-8')
list = f.readlines()
print(list)
f.close()

print("----------------------------- seek() --------------------------------")

f = open(root_paths + "Python_base/src/resources/file/folder1/textIO.txt", "r",
         encoding='utf-8')
f.seek(12)  # 移动到文件的第六个字节

tell = f.tell()
print("指针所在位置：", tell)

readline = f.readline()
print(readline)

f.close()
