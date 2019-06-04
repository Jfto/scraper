# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './LayoutFiles/PleaseWait/widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.setFixedSize(534, 339)
        Widget.setStyleSheet("background:white")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(10, -10, 521, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 521, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Please Wait. Scraping"))
        self.label.setText(_translate("Widget", "Please Wait"))
        self.label_2.setText(_translate("Widget", "Scraping"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

