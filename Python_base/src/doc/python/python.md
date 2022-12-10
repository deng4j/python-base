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
- virtualenvwrapper：virtualenv 的一组扩展。可以方便的创建、删除、复制、切换不同的虚拟环境。
  - pip install virtualenvwrapper       （Linux系统使用命令）
  - pip install virtualenvwrapper-win   （windows系统使用命令）

**配置虚拟环境：**

1. 安装virtualenv：pip install virtualenv
   - 安装后会在python的bin目录下有一个可执行文件virtualenv 
2. 创建虚拟模块：mkvirtualenv [虚拟环境名字]
3. 选择一个python解释器来创建虚拟化环境：virtualenv -p /usr/bin/python3.8 [虚拟环境名字]
4. 建立虚拟环境后，需要激活虚拟模块：

- Windows：虚拟环境的位置的Scripts文件夹中打开命令行输入：activate 或者 .\activate.bat
- mac：source activate

5. 进入指定虚拟环境：workon [虚拟环境名字]

- 查看当前虚拟环境安装的模块：workon 或 lsvirtualenv

6. 退出虚拟环境：deactivate.bat

删除虚拟环境：rmvirtualenv [虚拟环境名字]

**pycharm创建虚拟环境**就很简单：Project Interpreter中Add，然后给虚拟环境指定一个空目录位置，和基本解释器即可。可以勾选： Make available to all projects可用于所有项目、Inherit global site-packages继承全局站点软件包。

虚拟环境有scrapy库而解释器没有，不能直接使用scrpay命令：
       1.  ln -s /Library/Frameworks/Python.framework/Versions/Python3.9/bin/scrapy /usr/local/bin/scrapy
              2.  /venv/bin/python -m scrpay（虚拟环境路径的python，推荐）

# 命令


```css
python -h：查看python介绍
    -V：查看当前版本
    -c cmd ：作为字符串传入的程序（终止选项列表）
python -m module：去可执行文件python环境的标准库中搜索，将模块当作脚本使用，并以__main__模块执行其内容。

.../venv/bin/python -m scrapy crawl baidu：
	实际上运行的是.../venv/lib/python3.9/site-packages/scrapy/commands/crawl.py
.../venv/bin/python -m PyQt5.uic.pyuic：
	实际运行的是.../venv/lib/python3.9/site-packages/PyQt5/uic/pyuic.py

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

# Anaconda

Anaconda（[官方网站](https://link.zhihu.com/?target=https%3A//www.anaconda.com/download/%23macos)）就是可以便捷获取包且对包能够进行管理，同时对环境可以统一管理的发行版本。Anaconda包含了conda、Python在内的超过180个科学包及其依赖项。



# pip和conda

**pip是用于安装和管理软件包的包管理器：**

- 仅适用于Python

- 安装包时**或许**会直接忽略依赖项而安装，仅在结果中提示错误。

- 依赖检查：

  ① **不一定**会展示所需其他依赖包。

  ② 安装包时**或许**会直接忽略依赖项而安装，仅在结果中提示错误。

- 维护多个环境难度较大。
- 在系统自带Python中包的更新/回退版本/卸载将影响其他程序。



**conda是包及其依赖项和环境的管理工具：**

- 适用语言：Python, R, Ruby, Lua, Scala, Java, JavaScript, C/C++, FORTRAN。

-  适用平台：Windows, macOS, Linux

-  conda包和环境管理器包含于Anaconda的所有版本当中。

- 用途：

  ① 快速安装、运行和升级包及其依赖项。

  ② 在计算机中便捷地创建、保存、加载和切换环境。

- 依赖检查：

  ① 列出所需其他依赖包。

  ② 安装包时自动安装其依赖项。

  ③ 可以便捷地在包的不同版本中自由切换。

- 比较方便地在不同环境之间进行切换，环境管理较为简单。
- 不会影响系统自带Python。

如果你需要的包要求不同版本的Python，你无需切换到不同的环境，因为conda同样是一个环境管理器。



# GIL（全局解释器锁）

GIL（全局解释器锁）是最流程的CPython解释器（平常称为 Python）中的一个技术术语，其本质上类似操作系统的 Mutex。

GIL的功能是：在CPython解释器中执行的每一个Python线程，Thread 1、2、3 轮流执行，每一个线程在开始执行时，都会锁住 GIL，以阻止别的线程执行；同样的，每一个线程执行完一段后，会释放 GIL，以允许别的线程开始利用资源。

![Alt](images/2-1ZS012105L23.gif)

间隔式检查（check_interval）：CPython 解释器会去轮询检查线程GIL的锁住情况，每隔一段时间，Python解释器就会强制当前线程去释放GIL，这样别的线程才能有执行的机会。

有了 GIL，并不意味着 Python 程序员就不用去考虑线程安全了，因为即便 GIL 仅允许一个 Python 线程执行，但别忘了 Python 还有 check interval 这样的抢占机制。

接触GIL限制：

- 别用多线程
- 底层实现考虑其他东西
