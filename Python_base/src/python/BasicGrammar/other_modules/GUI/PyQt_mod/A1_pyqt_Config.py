"""
pip install PyQt5
pip install pyqt5-tools
pip install PyQt5-stubs # 可有可无

Qt Designer：通过拖拽的方式放置控件，并实时查看控件效果进行快速UI设计
    最终生成.ui文件（实质上是XML格式的文件），可以通过pyuic5工具转换成.py文件
Qt Designer配置：
    Pycharm中Settings - Tools - External Tools：
        Name: QtDisigner
        Program : .../site-packages/qt5_applications/Qt/bin/Designer.app
        Working directory: $FileDir$
    汉化：designer_zh_CN.qm放在.../site-packages/qt5_applications/Qt/translations


PyUIC配置：把Qt Designer生成的.ui文件换成.py文件。
    Pycharm中Settings - Tools - External Tools：
        Name: PyUIC
        Program : .../bin/python # 当前Python目录
        Arguments: -m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py
        Working directory: $FileDir$

PyRCC配置：PyRCC主要是把编写的.qrc资源文件换成.py文件。
    Pycharm中Settings - Tools - External Tools：
        Name: PyRCC
        Program : .../bin/python # 当前Python目录
        Arguments: -m PyQt5.uic.pyrcc_main $FileName$ -o $FileNameWithoutExtension$_rc.py
        Working directory: $FileDir$
"""
