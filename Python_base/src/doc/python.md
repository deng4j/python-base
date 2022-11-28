# 解释器

Python解释器（interpreter）在执行任何一个Python程序文件时，首先进行的动作都是先对文件中的Python源代码进行编译，编译的主要结果是产生一组Python的字节码（byte code），然后将编译的结果交给Python虚拟机（Virtual Machine），由虚拟机按照顺序一条一条地执行字节码，从而完成对Python程序的执行动作。

PyCodeObject对象是其真正的编译结果，一般保存在内存中。可以按照规则保存为.pyc文件，如使用' python -m compileall -b . '对.py文件进行编译保存。

pyc文件是由.py文件经过编译后生成的字节码文件，其加载速度相对于之前的.py文件有所提高，而且还可以实现源码隐藏，以及一定程度上的反编译。因此，不同版本的python可能运行不了同一个pyc文件。

# 虚拟环境

虚拟环境是Python解释器的一个副本环境，在这个环境中可以安装其它第三方Python包，在虚拟环境中安装的Python包不会影响全局环境中的包。

我们进入到哪个虚拟环境，这个虚拟环境下的可执行文件就可以直接使用，如bin目录下的pip。

**虚拟环境：**

- p：非常简单的交互式 python 版本管理工具。
- pyenv：简单的 Python 版本管理工具。
- Vex：可以在虚拟环境中执行命令
- virtualenv：创建独立 Python 环境的工具。
- virtualenvwrapper：virtualenv 的一组扩展。

**配置虚拟环境：**

​    1.配置虚拟环境：pip install virtualenv
​                    pip install virtualenvwrapper       （Linux系统使用命令）
​                    pip install virtualenvwrapper-win   （windows系统使用命令）

​    2.创建虚拟模块：mkvirtualenv [虚拟环境名字]

​    3.virtualenv -p /usr/bin/python3.8 [虚拟环境名字]：给虚拟环境指定解释器

​    4.进入指定虚拟环境：workon [虚拟环境名字]
​      4.1查看当前虚拟环境安装的模块：workon 或 lsvirtualenv

​    5.建立虚拟环境后，需要激活虚拟模块：虚拟环境的位置的Scripts文件夹中打开命令行输入：activate 或者 .\activate.bat

​    6.退出虚拟环境：deactivate.bat

删除虚拟环境：rmvirtualenv [虚拟环境名字]

**pycharm创建虚拟环境**就很简单：Project Interpreter中Add，然后给虚拟环境指定一个空目录位置，和基本解释器即可。可以勾选： Make available to all projects可用于所有项目、Inherit global site-packages继承全局站点软件包

虚拟环境有scrapy库而解释器没有，不能直接使用scrpay命令：
       1.  ln -s /Library/Frameworks/Python.framework/Versions/Python3.9/bin/scrapy /usr/local/bin/scrapy
       2.  /venv/bin/python -m scrpay（虚拟环境路径的python，推荐）

# 命令


```css
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
```