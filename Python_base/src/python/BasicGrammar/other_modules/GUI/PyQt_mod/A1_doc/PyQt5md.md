# 基础配置

## 安装模块

```css
pip install PyQt5
pip install pyqt5-tools
pip install PyQt5-stubs # 方便看代码的,可有可无
```

## 工具配置 

**1.Qt Designer配置**

Qt Designer：通过拖拽的方式放置控件，并实时查看控件效果进行快速UI设计。

最终生成.ui文件（实质上是XML格式的文件），可以通过pyuic5工具转换成.py文件。

Qt Designer配置在Pycharm中：Settings - Tools - External Tools

```css
Name: QtDisigner
Program : .../site-packages/qt5_applications/Qt/bin/Designer.app
Working directory: $FileDir$
```

汉化：designer_zh_CN.qm放在.../site-packages/qt5_applications/Qt/translations

**2.PyUIC配置**

PyUIC：把Qt Designer生成的.ui文件换成.py文件。

Pycharm中Settings - Tools - External Tools：

```css
Name: PyUIC
Program : .../bin/python # 当前Python目录
Arguments: -m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py
Working directory: $FileDir$
```

**3.PyRCC配置**

PyRCC：PyRCC主要是把编写的.qrc资源文件换成.py文件。

Pycharm中Settings - Tools - External Tools：

```css
Name: PyRCC
Program : .../bin/python # 当前Python目录
Arguments: -m PyQt5.uic.pyrcc_main $FileName$ -o $FileNameWithoutExtension$_rc.py
Working directory: $FileDir$
```

# 缓存位置

/Users/deng4j/.designer



# 打包

https://github.com/mherrmann/fbs-tutorial

