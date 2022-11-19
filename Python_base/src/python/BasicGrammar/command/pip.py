import platform

"""
简介：Python有两个著名的包管理工具easy_install和pip。在Python2.7的安装包中，easy_install是默认安装的，而pip需要我们
手动安装。随着Python版本的提高，easy_install已经逐渐被淘汰，但是一些比较老的第三方库，在现在仍然只能通过
easy_install进行安装。目前，pip已经成为主流的安装工具，自Python2 >=2.7.9或者Python3.4以后默认都安装有pip。

pip也有pip、pip2、pip3之分。pip是从属于Python的，对应的pip负责给对应的Python安装第三方模块。
我们不要关心pip后面跟的数字，核心的问题是这个pip命令对应的是哪个Python解释器。

安装pip：
    1.使用easy_install安装： 各种进入到easy_install脚本的目录下，然后运行easy_inatall pip
    2.使用get-pip.py安装： 在下面的url下载get-pip.py脚本 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        然后运行：python get-pip.py 这个脚本会同时安装setuptools和wheel工具。
    3.在linux下使用包管理工具安装pip： 例如，ubuntu下：sudo apt-get install python-pip。Fedora系下：sudo yum install python-pip
    4.在windows下安装pip： 在......Python\Python38\Scripts下运行easy_install pip进行安装。
刚安装完毕的pip可能需要先升级一下自身： 在Linux或masOS中：pip install -U pip 在windows中：python -m pip install -U pip

Python路径和版本：pip -V
安装特定版本的package，通过使用==, >=, <=, >, <来指定一个版本号：pip install 'Markdown<2.0' 或 pip install 'Markdown>2.0,<2.0.3
    避免没配置python环境变量：python -m pip install pip==22.2.2
指定安装位置：pip install django --target=D:\development\venv3.8.5\Lib\site-packages
安装包：pip install mysqlclient-1.4.6-cp39-cp39-win_amd64.whl
安装包：pip install Flask-WTF-0.10.0.tar.gz
卸载已安装的库：pip uninstall pillow
列出已经安装的库：pip list
将已经安装的库列表保存到文本文件中：pip freeze > requirements.txt
根据依赖文件批量安装库：pip install -r requirements.txt
使用wheel文件安装：pip install pillow-4.2xxxxxxx.whl
搜索包：pip search <搜索关键字>
查看某个已安装包：pip show --files package_name
检查哪些包需要更新：pip list --outdated
升级包：pip install --upgrade package_name
升级pip：pip install -U pip
卸载包：pip uninstall package_name

pip源的选择：
    如豆瓣：pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com pillow
    指定阿里镜像版本：pip install torch==1.7.1 -i https://mirrors.aliyun.com/pypi/simple/
    清华：https://pypi.tuna.tsinghua.edu.cn/simple
    中国科技大学：https://pypi.mirrors.ustc.edu.cn/simple/
    华中理工大学：http://pypi.hustunique.com/
    山东理工大学：http://pypi.sdutlinux.org/
    
Win32 -> 指的就是Windows系统；
64 bit- > 指的是Windows是64位的；
AMD64 -> 指的就是 CPU是x64的
"""

print(platform.architecture())  # 查看平台支持
