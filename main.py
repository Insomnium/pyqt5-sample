#coding: utf8
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType

app = QApplication(sys.argv)
app.setApplicationName('python')
form_class, base_class = loadUiType('window.ui')


class MainWindow(QDialog, form_class):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        self.setupUi(self)
        self.__unpressed = True


    def pressMeBtnClicked(self):

        self.lineEdit.setText('Pressed' if self.__unpressed else 'Unpressed')
        self.__unpressed = not self.__unpressed

form = MainWindow()
form.setWindowTitle('python')
form.show()
sys.exit(app.exec_())