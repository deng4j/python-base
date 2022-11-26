"""
pip install pyinstaller # 打包工具，安装后python环境目录下会增加一个pyinstaller.exe程序
    选项：
        -F，-onefile	产生单个的可执行文件
        -D，--onedir	产生一个目录（包含多个文件）作为可执行程序
        -a，--ascii	不包含 Unicode 字符集支持
        -d，--debug	产生 debug 版本的可执行文件
        -w，--windowed，--noconsolc	指定程序运行时不显示命令行窗口（仅对 Windows 有效）
        -c，--nowindowed，--console	指定使用命令行窗口运行程序（仅对 Windows 有效）
        -o DIR，--out=DIR	指定 spec 文件的生成目录。如果没有指定，则默认使用当前目录来生成 spec 文件
        -p DIR，--path=DIR	设置 Python 导入模块的路径（和设置 PYTHONPATH 环境变量的作用相似）。也可使用路径分隔符（Windows 使用分号，Linux 使用冒号）来分隔多个路径
        -n NAME，--name=NAME	指定项目（产生的 spec）名字。如果省略该选项，那么第一个脚本的主文件名将作为 spec 的名字
    1.在主函数所在文件main.py打包
        # 多文件，
        pyinstaller -D main.py
        # 单个可执行文件
        pyinstaller -F main.py
    2.在当前目录下dist文件夹里就是打包好的可执行程序。这个时候运行会出现一个控制台，如果出现错误会在控制台中打印出来，可以用于测试；
    如果测试没问题就可以去掉控制台窗口（使用-w命令）：
        pyinstaller -D -w main.py
    3.给可执行文件添加图标（使用-i 命令）：
        pyinstaller -D -w -i icon.ico main.py
    4.使用upx压缩可执行文件 https://upx.github.io/ ，把可upx.exe放在虚拟环境bin目录
        手动执行：
            upx *.dll
            upx *.exe
    4.报错Qt platform plugin could be initialized
        先关掉upx，也就是在pyinstaller后加上参数--noupx，重新运行打包一次
"""