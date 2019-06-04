# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './LayoutFiles/Menu/widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import DBSearch
import DBDialog
import ScraperUI
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Widget(object):
    btnActive = True
    def setupUi(self, Widget):
        self.MainWidget = Widget
        Widget.setObjectName("Widget")
        Widget.setFixedSize(425, 450)
        self.ScraperBTN = QtWidgets.QPushButton(Widget)
        self.ScraperBTN.setGeometry(QtCore.QRect(0, 0, 421, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.ScraperBTN.setFont(font)
        self.ScraperBTN.setObjectName("ScraperBTN")
        self.DBSearchBTN = QtWidgets.QPushButton(Widget)
        self.DBSearchBTN.setGeometry(QtCore.QRect(0, 110, 421, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.DBSearchBTN.setFont(font)
        self.DBSearchBTN.setObjectName("DBSearchBTN")
        self.AdminBTN = QtWidgets.QPushButton(Widget)
        self.AdminBTN.setGeometry(QtCore.QRect(0, 330, 421, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.AdminBTN.setFont(font)
        self.AdminBTN.setStyleSheet("color:grey")
        self.AdminBTN.setObjectName("AdminBTN")
        self.ConfigBTN = QtWidgets.QPushButton(Widget)
        self.ConfigBTN.setGeometry(QtCore.QRect(0, 220, 421, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.ConfigBTN.setFont(font)
        self.ConfigBTN.setStyleSheet("color:grey")
        self.ConfigBTN.setObjectName("ConfigBTN")
        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        self.DBSearchBTN.clicked.connect(self.DbDialog)
        self.ScraperBTN.clicked.connect(self.OpenScraper)
    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.ScraperBTN.setText(_translate("Widget", "Scraper"))
        self.DBSearchBTN.setText(_translate("Widget", "Database"))
        self.AdminBTN.setText(_translate("Widget", "Admin"))
        self.ConfigBTN.setText(_translate("Widget", "Options"))
    def DbDialog(self):
        if self.btnActive == True:
            self.btnActive = False
            self.window = QtWidgets.QWidget()
            self.ui = DBDialog.Ui_Widget()
            self.ui.setupUi(self.window)
            self.ui.sendSelf(self)
            self.window.show()
    def OpenScraper(self):
        if self.btnActive == True:
            self.window = QtWidgets.QWidget()
            self.ui = ScraperUI.Ui_Widget()
            self.ui.setupUi(self.window)
            self.MainWidget.hide()
            self.window.show()
    def hide(self):
        self.MainWidget.hide()
if __name__ == "__main__":
    import sys
    from twisted.internet import reactor
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

