"""
Python解释器（interpreter）在执行任何一个Python程序文件时，首先进行的动作都是先对文件中的Python源代码进行编译，
    编译的主要结果是产生一组Python的字节码（byte code），然后将编译的结果交给Python虚拟机（Virtual Machine），
    由虚拟机按照顺序一条一条地执行字节码，从而完成对Python程序的执行动作。

PyCodeObject对象是其真正的编译结果，一般保存在内存中。可以按照规则保存为.pyc文件，如使用' python -m compileall -b . '
    对.py文件进行编译保存。

pyc文件是由.py文件经过编译后生成的字节码文件，其加载速度相对于之前的.py文件有所提高，而且还可以实现源码隐藏，
    以及一定程度上的反编译。因此，不同版本的python可能运行不了同一个pyc文件。
"""

"""
python -h：查看python介绍
    -V：查看当前版本
    -c cmd ：作为字符串传入的程序（终止选项列表）

python -m module：去标准库中搜索，将模块当作脚本使用，并以 __main__模块执行其内容。

python test.py arg1 arg2 arg3：执行该文件，并赋予参数。

where python：查看python解释器路径
which python：查看python的路径
python：进入终端交互模式，可以编写代码
exit()：退出终端交互模式

python setup.py sdist 源码压缩包 生成dist文件
python setup.py bdist 二进制发布包 结果不包括setup.py的二进制文件
python setup.py sdist --formats=zip,tar 压缩成成不同格式的源文件
python setup.py bdist_egg .egg格式
python setup.py bdist_wheel .whl格式
python setup.py bdist_wininst windows下面的文件exe
"""