from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import File_Download
import sys


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = File_Download.Ui_Dialog()
        self.ui.setupUi(self)

    def cleanDir(self):
        self.ui.textEdit_dir.clear()

    def cleanURL(self):
        self.ui.textEdit_url.clear()

    def download(self):
        self.ui.textEdit_notice.clear()
        path = self.ui.textEdit_dir.toPlainText()
        url = self.ui.textEdit_url.toPlainText()
        flag = self.urllib_download(IMAGE_URL=url, folderPath=path, suffix='.png')
        if flag is False:
            self.ui.textEdit_notice.setTextColor(QtGui.QColor('red'))
            self.ui.textEdit_notice.setText('下载失败！！！')
        else:
            self.ui.textEdit_notice.setTextColor(QtGui.QColor('green'))
            self.ui.textEdit_notice.setText('下载成功')
            self.cleanURL()

    def urllib_download(self, IMAGE_URL, folderPath, suffix):
        from urllib.request import urlretrieve
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        import time
        now = int(round(time.time() * 1000000))
        folderPath = folderPath + '/' + str(now) + suffix
        try:
            urlretrieve(IMAGE_URL, folderPath)
        except:
            return False
        return True


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())
