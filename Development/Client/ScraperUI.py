#DBSearch created and owned by Jeremy Felts
#Code Completion: TBD
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess
from time import sleep
import PleaseWait
import requests
class Ui_Widget(object):
    Selected = None
    def setupUi(self, Widget):
        self.window = QtWidgets.QWidget()
        self.ui = PleaseWait.Ui_Widget()
        self.ui.setupUi(self.window)
        self.widget = Widget
        Widget.setObjectName("Widget")
        # Widget.showMaximized()
        Widget.setFixedSize(400, 245)
        
        self.KithScraper = QtWidgets.QPushButton(Widget)
        self.KithScraper.setGeometry(QtCore.QRect(0, 0, 171, 31))
        self.KithScraper.setObjectName("KithScraper")
        self.KithScraper.setStyleSheet("background:white; border:5px solid black;")
        self.StonyIslandScraper = QtWidgets.QPushButton(Widget)
        self.StonyIslandScraper.setGeometry(QtCore.QRect(0, 30, 171, 31))
        self.StonyIslandScraper.setObjectName("StonyIslandScraper")
        self.StonyIslandScraper.setStyleSheet("background: white; border: 1px solid black; color:grey")
        self.UndefeatedScraper = QtWidgets.QPushButton(Widget)
        self.UndefeatedScraper.setGeometry(QtCore.QRect(0, 60, 171, 31))
        self.UndefeatedScraper.setObjectName("UndefeatedScraper")
        self.UndefeatedScraper.setStyleSheet("background:white; border:5px solid black;")
        self.DSMScraper = QtWidgets.QPushButton(Widget)
        self.DSMScraper.setGeometry(QtCore.QRect(0, 90, 171, 31))
        self.DSMScraper.setObjectName("DSMScraper")
        self.DSMScraper.setStyleSheet("background: white; border: 1px solid black; color:grey")
        self.ConceptsScraper = QtWidgets.QPushButton(Widget)
        self.ConceptsScraper.setGeometry(QtCore.QRect(0, 120, 171, 31))
        self.ConceptsScraper.setObjectName("ConceptsScraper")
        self.ConceptsScraper.setStyleSheet("background:white; border:5px solid black;")
        self.BackBTN = QtWidgets.QPushButton(Widget)
        self.BackBTN.setGeometry(QtCore.QRect(0, 210, 61, 31))
        self.BackBTN.setObjectName("BackBTN")
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setGeometry(QtCore.QRect(170, 0, 231, 191))
        self.frame.setStyleSheet("background:white; ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.NameTitle = QtWidgets.QLabel(self.frame)
        self.NameTitle.setGeometry(QtCore.QRect(10, 5, 100, 16))
        self.NameTitle.setObjectName("NameTitle")
        self.NameTXT = QtWidgets.QLabel(self.frame)
        self.NameTXT.setGeometry(QtCore.QRect(10, 20, 100, 16))
        self.NameTXT.setObjectName("NameTXT")
        self.TimeTXT = QtWidgets.QLabel(self.frame)
        self.TimeTXT.setGeometry(QtCore.QRect(10, 70, 200, 16))
        self.TimeTXT.setObjectName("TimeTXT")
        self.LastRan = QtWidgets.QLabel(self.frame)
        self.LastRan.setGeometry(QtCore.QRect(10, 50, 100, 16))
        self.LastRan.setObjectName("LastRan")
        self.GoBtn = QtWidgets.QPushButton(Widget)
        self.GoBtn.setGeometry(QtCore.QRect(230, 190, 171, 31))
        self.GoBtn.setStyleSheet("background:green; color:white; ")
        self.GoBtn.setObjectName("GoBtn")
        self.BackBTN.clicked.connect(self.BackBTNClicked)
        self.KithScraper.clicked.connect(self.SelKith)
        #self.StonyIslandScraper.clicked.connect(self.SelStony)
        self.UndefeatedScraper.clicked.connect(self.SelUNDF)
        self.ConceptsScraper.clicked.connect(self.SelConcepts)
        self.GoBtn.clicked.connect(self.StartScrape)
        self.retranslateUi(Widget)
        def setTimes():
            r = requests.get('http://18.218.171.89/GetTZ')
            self.ConceptsScraper.LastUpdated = r.json()[0]['LastCompletedConcept']
            self.KithScraper.LastUpdated = r.json()[1]['LastCompletedKith']
            self.UndefeatedScraper.LastUpdated = r.json()[2]['LastCompletedUndefeated']
            self.TimeTXT.setText(self.KithScraper.LastUpdated)
            print(['Undefeated',self.UndefeatedScraper.LastUpdated,'Kith',self.KithScraper.LastUpdated,'Concepts',self.ConceptsScraper.LastUpdated])
        setTimes()
        QtCore.QMetaObject.connectSlotsByName(Widget)
    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.KithScraper.setText(_translate("Widget", "Kith Scraper"))
        self.StonyIslandScraper.setText(_translate("Widget", "Stony Island Scraper"))
        self.UndefeatedScraper.setText(_translate("Widget", "Undefeated Scraper"))
        self.DSMScraper.setText(_translate("Widget", "DSM Scraper"))
        self.ConceptsScraper.setText(_translate("Widget", "Concepts Scraper"))
        self.BackBTN.setText(_translate("Widget", "Menu"))
        self.NameTitle.setText(_translate("Widget", "Name:"))
        self.NameTXT.setText(_translate("Widget", "KITH"))
        self.LastRan.setText(_translate("Widget", "Last Ran:"))
        self.GoBtn.setText(_translate("Widget", "Start Scraper"))
        
    def SelKith(self):
        if self.Selected != None:
            self.Selected.setStyleSheet("background:white; border:5px solid black;")
        self.Selected = self.KithScraper
        self.Selected.setStyleSheet("background:white; border:5px solid blue;")
        self.NameTXT.setText("Kith")
        self.TimeTXT.setText(self.KithScraper.LastUpdated)

    def SelStony(self):
        if self.Selected != None:
            self.Selected.setStyleSheet("background:white; border:5px solid black;")
        self.Selected = self.StonyIslandScraper
        self.Selected.setStyleSheet("background:white; border:5px solid blue;")
        self.NameTXT.setText("Stony Island")
    def SelUNDF(self):
        if self.Selected != None:
            self.Selected.setStyleSheet("background:white; border:5px solid black;")
        self.Selected = self.UndefeatedScraper
        self.Selected.setStyleSheet("background:white; border:5px solid blue;")
        self.NameTXT.setText("Undefeated")
        self.TimeTXT.setText(self.UndefeatedScraper.LastUpdated)
    def SelConcepts(self):
        if self.Selected != None:
            self.Selected.setStyleSheet("background:white; border:5px solid black;")
        self.Selected = self.ConceptsScraper
        self.Selected.setStyleSheet("background:white; border:5px solid blue;")
        self.NameTXT.setText("Concepts")
        self.TimeTXT.setText(self.ConceptsScraper.LastUpdated)
    def StartScrape(self):
        if self.Selected != None:
            if self.Selected == self.KithScraper:
                requests.get('http://18.218.171.89/Start/Kith')
            elif self.Selected == self.UndefeatedScraper:
                requests.get('http://18.218.171.89/Start/Undefeated')
            elif self.Selected == self.ConceptsScraper:
                requests.get('http://18.218.171.89/Start/Concept')
    def BackBTNClicked(self):
        import Menu
        self.widget.hide()
        self.menuBASE = QtWidgets.QWidget()
        self.menuUI = Menu.Ui_Widget()
        self.menuUI.setupUi(self.menuBASE)
        self.menuBASE.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

