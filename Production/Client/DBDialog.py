# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './LayoutFiles/DBDialog/widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import Menu
import DBSearch
class Ui_Widget(object):
    Selected = None
    MainWidget = None
    def setupUi(self, Widget):
        Widget.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowStaysOnTopHint
            )
        Widget.setObjectName("Widget")
        Widget.setFixedSize(200, 325)
        self.DialogWidget = Widget
        self.KithShoe = QtWidgets.QPushButton(Widget)
        self.KithShoe.setGeometry(QtCore.QRect(0, 0, 201, 31))
        self.KithShoe.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:grey;")
        self.KithShoe.setObjectName("KithShoe")
        self.KithShoe.clickable = True
        self.CancelBTN = QtWidgets.QPushButton(Widget)
        self.CancelBTN.setGeometry(QtCore.QRect(0, 280, 201, 41))
        self.CancelBTN.setStyleSheet("border-radius:20; background:red; border:1px solid white;color:white;")
        self.CancelBTN.setObjectName("CancelBTN")
        self.GoBTN = QtWidgets.QPushButton(Widget)
        self.GoBTN.setGeometry(QtCore.QRect(0, 240, 201, 41))
        self.GoBTN.setStyleSheet("border-radius:20; background:green; border:1px solid white;color:white;")
        self.GoBTN.setObjectName("GoBTN")
        self.KithOther = QtWidgets.QPushButton(Widget)
        self.KithOther.setGeometry(QtCore.QRect(0, 30, 201, 31))
        self.KithOther.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:grey;")
        self.KithOther.setObjectName("KithOther")
        self.KithOther.clickable = True
        self.StoneIslandShoe = QtWidgets.QPushButton(Widget)
        self.StoneIslandShoe.setGeometry(QtCore.QRect(0, 60, 201, 31))
        self.StoneIslandShoe.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:grey;")
        self.StoneIslandShoe.setObjectName("StoneIslandShoe")
        self.StoneIslandShoe.clickable = False
        self.StoneIslandOther = QtWidgets.QPushButton(Widget)
        self.StoneIslandOther.setGeometry(QtCore.QRect(0, 90, 201, 31))
        self.StoneIslandOther.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:grey;")
        self.StoneIslandOther.setObjectName("StoneIslandOther")
        self.StoneIslandOther.clickable = False
        self.UndefeatedShoe = QtWidgets.QPushButton(Widget)
        self.UndefeatedShoe.setGeometry(QtCore.QRect(0, 120, 201, 31))
        self.UndefeatedShoe.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:grey;")
        self.UndefeatedShoe.setObjectName("UndefeatedShoe")
        self.UndefeatedShoe.clickable = True
        self.UndefeatedOther = QtWidgets.QPushButton(Widget)
        self.UndefeatedOther.setGeometry(QtCore.QRect(0, 150, 201, 31))
        self.UndefeatedOther.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:grey;")
        self.UndefeatedOther.setObjectName("UndefeatedOther")
        self.UndefeatedOther.clickable = True
        self.ConceptsShoe = QtWidgets.QPushButton(Widget)
        self.ConceptsShoe.setGeometry(QtCore.QRect(0, 180, 201, 31))
        self.ConceptsShoe.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:grey;")
        self.ConceptsShoe.setObjectName("ConceptsShoe")
        self.ConceptsShoe.clickable = True
        self.ConceptOther = QtWidgets.QPushButton(Widget)
        self.ConceptOther.setGeometry(QtCore.QRect(0, 210, 201, 31))
        self.ConceptOther.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:grey;")
        self.ConceptOther.setObjectName("ConceptOther")
        self.ConceptOther.clickable = True
        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.KithShoe.setText(_translate("Widget", "Kith Shoes"))
        self.CancelBTN.setText(_translate("Widget", "Cancel"))
        self.GoBTN.setText(_translate("Widget", "Go"))
        self.KithOther.setText(_translate("Widget", "Kith Other"))
        self.StoneIslandShoe.setText(_translate("Widget", "Stoney Island Shoe"))
        self.StoneIslandOther.setText(_translate("Widget", "Stone Island Other"))
        self.UndefeatedShoe.setText(_translate("Widget", "Undefeated Shoe"))
        self.UndefeatedOther.setText(_translate("Widget", "Undefeated Other"))
        self.ConceptsShoe.setText(_translate("Widget", "Concepts Shoe"))
        self.ConceptOther.setText(_translate("Widget", "Concept Other"))
        self.CancelBTN.clicked.connect(self.Cancel)
        if self.KithShoe.clickable == True:
            self.KithShoe.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.KithShoe.clicked.connect(self.SelKithShoe)
        if self.KithOther.clickable == True:
            self.KithOther.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.KithOther.clicked.connect(self.SelKithOther)
        if self.UndefeatedShoe.clickable == True:
            self.UndefeatedShoe.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.UndefeatedShoe.clicked.connect(self.SelUndefeatedShoe)
        if self.UndefeatedOther.clickable == True:
            self.UndefeatedOther.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.UndefeatedOther.clicked.connect(self.SelUndefeatedOther)
        if self.ConceptsShoe.clickable == True:
            self.ConceptsShoe.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.ConceptsShoe.clicked.connect(self.SelConceptsShoe)
        if self.ConceptOther.clickable == True:
            self.ConceptOther.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.ConceptOther.clicked.connect(self.SelConceptsOther)
        self.GoBTN.clicked.connect(self.GoBtnClick)
    def Cancel(self):
        self.MainWidget.btnActive = True
        self.DialogWidget.hide()
    def sendSelf(self, input):
        self.MainWidget = input
    def GoBtnClick(self):
        if self.Selected != None:
            self.window = QtWidgets.QWidget()
            self.ui = DBSearch.Ui_MainWindow()
            if self.Selected == self.KithShoe:
                self.ui.setupUi(self.window, db="KithDB", catagory="Shoes")
            elif self.Selected == self.KithOther:
                self.ui.setupUi(self.window, db="KithDB", catagory="Other")
            elif self.Selected == self.UndefeatedShoe:
                self.ui.setupUi(self.window, db="UndefeatedDB", catagory="Shoes")
            elif self.Selected == self.UndefeatedOther:
                self.ui.setupUi(self.window, db="UndefeatedDB", catagory="Other")
            elif self.Selected == self.StoneIslandShoe:
                self.ui.setupUi(self.window, db="StoneIslandDB", catagory="Shoes")
            elif self.Selected == self.StoneIslandOther:
                self.ui.setupUi(self.window, db="StoneIslandDB", catagory="Other")
            elif self.Selected == self.ConceptsShoe:
                self.ui.setupUi(self.window, db="ConceptsDB", catagory="Shoes")
            elif self.Selected == self.ConceptOther:
                self.ui.setupUi(self.window, db="ConceptsDB", catagory="Other")
            self.window.show()
            self.MainWidget.hide()
            self.DialogWidget.hide()
    def SelKithShoe(self):
        if self.KithShoe.clickable == True:
            if self.Selected != None:
                print("yes")
                self.Selected.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.Selected = self.KithShoe
            self.KithShoe.setStyleSheet("border-radius:0; border:5px solid blue; background:white; color:black;")
    def SelKithOther(self):
        if self.KithOther.clickable == True:
            if self.Selected != None:
                self.Selected.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.Selected = self.KithOther
            self.KithOther.setStyleSheet("border-radius:0; border:5px solid blue; background:white; color:black;")
    def SelUndefeatedShoe(self):
        if self.UndefeatedShoe.clickable == True:
            if self.Selected != None:
                self.Selected.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.Selected = self.UndefeatedShoe
            self.UndefeatedShoe.setStyleSheet("border-radius:0; border:5px solid blue; background:white; color:black;")
    def SelUndefeatedOther(self):
        if self.UndefeatedOther.clickable == True:
            if self.Selected != None:
                self.Selected.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.Selected = self.UndefeatedOther
            self.UndefeatedOther.setStyleSheet("border-radius:0; border:5px solid blue; background:white; color:black;")
    def SelConceptsShoe(self):
        if self.ConceptsShoe.clickable == True:
            if self.Selected != None:
                self.Selected.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.Selected = self.ConceptsShoe
            self.ConceptsShoe.setStyleSheet("border-radius:0; border:5px solid blue; background:white; color:black;")
    def SelConceptsOther(self):
        if self.ConceptOther.clickable == True:
            if self.Selected != None:
                self.Selected.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.Selected = self.ConceptOther
            self.ConceptOther.setStyleSheet("border-radius:0; border:5px solid blue; background:white; color:black;")
    def SelStoneShoe(self):
        if self.StoneIslandShoe.clickable == True:
            if self.Selected != None:
                self.Selected.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.Selected = self.StoneIslandShoe
            self.StoneIslandShoe.setStyleSheet("border-radius:0; border:5px solid blue; background:white; color:black;")
    def SelStoneOther(self):
        if self.StoneIslandOther.clickable == True:
            if self.Selected != None:
                self.Selected.setStyleSheet("border-radius:0; border:5px solid black; background:white; color:black;")
            self.Selected = self.StoneIslandOther
            self.StoneIslandOther.setStyleSheet("border-radius:0; border:5px solid blue; background:white; color:black;")
    #Below Buttons NOT added. Commented to avoid false issues
    # def SelDSMShoe(self):
    #     if self.DSMShoe.clickable == True:
    #         if self.Selected != None:
    #             self.Selected.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:black;")
    #         self.Selected = self.DSMShoe
    #         self.DSMShoe.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:blue;")
    # def SelDSMOther(self):
    #     if self.DSMOther.clickable == True:
    #         if self.Selected != None:
    #             self.Selected.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:black;")
    #         self.Selected = self.DSMOther
    #         self.DSMOther.setStyleSheet("border-radius:0; border:1px solid black; background:white; color:blue;")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

