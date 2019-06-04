#DBSearch created and owned by Jeremy Felts
#Code Completion: 4/8/2019

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os
import sys
import requests
from io import BytesIO
import urllib
from time import sleep
import webbrowser
from tinydb import TinyDB, Query
import Menu
def PicRequest(url):
    return urllib.request.urlopen(url).read()
#region UI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow, db, catagory, search=None):
        self.MainWindow = MainWindow
        self.Name = ""
        self.url = ""
        self.image = None
        self.colors = ""
        self.price = ""
        self.value = 0
        self.search = search
        self.db = db
        self.catagory = catagory
        Q = Query()
        test_contains = lambda value, search: search.lower() in value.lower()
        if search == None:
            self.NameList = requests.get('http://18.218.171.89/'+str(catagory)+'/'+str(db)).json()
        else:
            self.NameList = requests.get('http://18.218.171.89/'+str(catagory)+'/'+str(db)+'/'+str(search)).json()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(721, 563)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setBaseSize(QtCore.QSize(721, 517))
        MainWindow.setStyleSheet("border: 1px solid black")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(430, 250, 261, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setBaseSize(QtCore.QSize(261, 271))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color: white;border: 1px solid grey;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setStyleSheet("border: 0px")
        self.label.setLineWidth(0)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 6, 161, 20))
        self.label_2.setStyleSheet("border: 0px")
        self.label_2.setLineWidth(0)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.label_4.setStyleSheet("border: 0px")
        self.label_4.setLineWidth(0)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(60, 30, 47, 13))
        self.label_6.setStyleSheet("border: 0px")
        self.label_6.setLineWidth(0)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 41, 20))
        self.label_5.setStyleSheet("border: 0px")
        self.label_5.setLineWidth(0)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 41, 20))
        self.label_7.setStyleSheet("border: 0px")
        self.label_7.setLineWidth(0)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(50, 50, 111, 20))
        self.label_8.setStyleSheet("border: 0px")
        self.label_8.setLineWidth(0)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(50, 200, 91, 20))
        self.pushButton.setStyleSheet("border: 0px; color: \"dark blue\"; text-decoration: underline;")
        self.pushButton.setObjectName("pushButton")
        self.OKBtn = QtWidgets.QPushButton(self.centralWidget)
        self.OKBtn.setGeometry(QtCore.QRect(350, 5, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OKBtn.sizePolicy().hasHeightForWidth())
        self.OKBtn.setSizePolicy(sizePolicy)
        self.OKBtn.setBaseSize(QtCore.QSize(41, 21))
        self.OKBtn.setObjectName("OKBtn")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(19, 6, 327, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setBaseSize(QtCore.QSize(327, 21))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: white;border: 1px solid grey;")
        self.backBtn = QtWidgets.QPushButton(self.centralWidget)
        self.backBtn.setGeometry(QtCore.QRect(640, 10, 51, 21))
        self.backBtn.setObjectName("backBtn")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 36, 80, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 530, 80, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.ItemIMG = QtWidgets.QLabel(self.centralWidget)
        self.ItemIMG.setGeometry(QtCore.QRect(430, 60, 261, 181))
        self.ItemIMG.setText("")
        self.defaultpixmap = QPixmap()
        self.defaultpixmap.loadFromData(PicRequest('https://ichef.bbci.co.uk/news/976/cpsprodpb/27C9/production/_103158101_tha.jpg'))
        self.ItemIMG.setPixmap(self.defaultpixmap)
        self.ItemIMG.setScaledContents(True)
        self.ItemIMG.setObjectName("ItemIMG")
        self.backBtn.clicked.connect(self.BckButtonClicked)
#region textBrowserFormat
        self.textBrowser_1 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_1.setGeometry(QtCore.QRect(20, 60, 371, 21))
        self.textBrowser_1.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_1.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 80, 371, 21))
        self.textBrowser_2.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 100, 371, 21))
        self.textBrowser_3.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 120, 371, 21))
        self.textBrowser_4.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(20, 140, 371, 21))
        self.textBrowser_5.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(20, 160, 371, 21))
        self.textBrowser_6.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(20, 180, 371, 21))
        self.textBrowser_7.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(20, 200, 371, 21))
        self.textBrowser_8.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(20, 220, 371, 21))
        self.textBrowser_9.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_10.setGeometry(QtCore.QRect(20, 240, 371, 21))
        self.textBrowser_10.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_11.setGeometry(QtCore.QRect(20, 260, 371, 21))
        self.textBrowser_11.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QPushButton(self.centralWidget)#
        self.textBrowser_12.setGeometry(QtCore.QRect(20, 280, 371, 21))
        self.textBrowser_12.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_13 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_13.setGeometry(QtCore.QRect(20, 300, 371, 21))
        self.textBrowser_13.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.textBrowser_14 = QtWidgets.QPushButton(self.centralWidget)#
        self.textBrowser_14.setGeometry(QtCore.QRect(20, 320, 371, 21))
        self.textBrowser_14.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.textBrowser_15 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_15.setGeometry(QtCore.QRect(20, 340, 371, 21))
        self.textBrowser_15.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.textBrowser_16 = QtWidgets.QPushButton(self.centralWidget)#
        self.textBrowser_16.setGeometry(QtCore.QRect(20, 360, 371, 21))
        self.textBrowser_16.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.textBrowser_17 = QtWidgets.QPushButton(self.centralWidget)#
        self.textBrowser_17.setGeometry(QtCore.QRect(20, 380, 371, 21))
        self.textBrowser_17.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.textBrowser_18 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_18.setGeometry(QtCore.QRect(20, 400, 371, 21))
        self.textBrowser_18.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.textBrowser_19 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_19.setGeometry(QtCore.QRect(20, 420, 371, 21))
        self.textBrowser_19.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.textBrowser_20 = QtWidgets.QPushButton(self.centralWidget)#
        self.textBrowser_20.setGeometry(QtCore.QRect(20, 440, 371, 21))
        self.textBrowser_20.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_20.setObjectName("textBrowser_20")
        self.textBrowser_21 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_21.setGeometry(QtCore.QRect(20, 460, 371, 21))
        self.textBrowser_21.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_21.setObjectName("textBrowser_21")
        self.textBrowser_22 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_22.setGeometry(QtCore.QRect(20, 480, 371, 21))
        self.textBrowser_22.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_22.setObjectName("textBrowser_22")
        self.textBrowser_23 = QtWidgets.QPushButton(self.centralWidget)
        self.textBrowser_23.setGeometry(QtCore.QRect(20, 500, 371, 21))
        self.textBrowser_23.setStyleSheet("border: 1px solid grey;")
        self.textBrowser_23.setObjectName("textBrowser_23")
#endregion

        #MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.textBrowserGroup = [self.textBrowser_1,self.textBrowser_2,self.textBrowser_3,self.textBrowser_4,self.textBrowser_5,self.textBrowser_6,self.textBrowser_7,self.textBrowser_8,self.textBrowser_9,self.textBrowser_10,self.textBrowser_11,self.textBrowser_12,self.textBrowser_13,self.textBrowser_14,self.textBrowser_15,self.textBrowser_16,self.textBrowser_17,self.textBrowser_18,self.textBrowser_19,self.textBrowser_20,self.textBrowser_21,self.textBrowser_22,self.textBrowser_23]
#region List functionality
        try:
            self.textBrowser_1.setText(self.NameList[0]["title"])
            self.textBrowser_1.Name = self.NameList[0]["title"]
            self.textBrowser_1.url = self.NameList[0]["href"]
            self.textBrowser_1.image = "https:"+self.NameList[0]["image"]
            self.textBrowser_1.price = self.NameList[0]["price"]
            self.textBrowser_1.colors = self.NameList[0]["colors"]
        except:
            self.textBrowser_1.setText("")
            self.textBrowser_1.Name = ""
            self.textBrowser_1.url = ""
            self.textBrowser_1.image = None
            self.textBrowser_1.price = ""
            self.textBrowser_1.colors = ""
        try:
            self.textBrowser_2.setText(self.NameList[1]["title"])
            self.textBrowser_2.Name = self.NameList[1]["title"]
            self.textBrowser_2.url = self.NameList[1]["href"]
            self.textBrowser_2.image = "https:"+self.NameList[1]["image"]
            self.textBrowser_2.price = self.NameList[1]["price"]
            self.textBrowser_2.colors = self.NameList[1]["colors"]
        except:
            self.textBrowser_2.setText("")
            self.textBrowser_2.Name = ""
            self.textBrowser_2.url = ""
            self.textBrowser_2.image = None
            self.textBrowser_2.price = ""
            self.textBrowser_2.colors = ""
        try:
            self.textBrowser_3.setText(self.NameList[2]["title"])
            self.textBrowser_3.Name = self.NameList[2]["title"]
            self.textBrowser_3.url = self.NameList[2]["href"]
            self.textBrowser_3.image = "https:"+self.NameList[2]["image"]
            self.textBrowser_3.price = self.NameList[2]["price"]
            self.textBrowser_3.colors = self.NameList[2]["colors"]
        except:
            self.textBrowser_3.setText("")
            self.textBrowser_3.Name = ""
            self.textBrowser_3.url = ""
            self.textBrowser_3.image = None
            self.textBrowser_3.price = ""
            self.textBrowser_3.colors = ""
        try:
            self.textBrowser_4.setText(self.NameList[3]["title"])
            self.textBrowser_4.Name = self.NameList[3]["title"]
            self.textBrowser_4.url = self.NameList[3]["href"]
            self.textBrowser_4.image = "https:"+self.NameList[3]["image"]
            self.textBrowser_4.price = self.NameList[3]["price"]
            self.textBrowser_4.colors = self.NameList[3]["colors"]
        except:
            self.textBrowser_4.setText("")
            self.textBrowser_4.Name = ""
            self.textBrowser_4.url = ""
            self.textBrowser_4.image = None
            self.textBrowser_4.price = ""
            self.textBrowser_4.colors = ""
        try:
            self.textBrowser_5.setText(self.NameList[4]["title"])
            self.textBrowser_5.Name = self.NameList[4]["title"]
            self.textBrowser_5.url = self.NameList[4]["href"]
            self.textBrowser_5.image = "https:"+self.NameList[4]["image"]
            self.textBrowser_5.price = self.NameList[4]["price"]
            self.textBrowser_5.colors = self.NameList[4]["colors"]
        except:
            self.textBrowser_5.setText("")
            self.textBrowser_5.Name = ""
            self.textBrowser_5.url = ""
            self.textBrowser_5.image = None
            self.textBrowser_5.price = ""
            self.textBrowser_5.colors = ""
        try:
            self.textBrowser_6.setText(self.NameList[5]["title"])
            self.textBrowser_6.Name = self.NameList[5]["title"]
            self.textBrowser_6.url = self.NameList[5]["href"]
            self.textBrowser_6.image = "https:"+self.NameList[5]["image"]
            self.textBrowser_6.price = self.NameList[5]["price"]
            self.textBrowser_6.colors = self.NameList[5]["colors"]
        except:
            self.textBrowser_6.setText("")
            self.textBrowser_6.Name = ""
            self.textBrowser_6.url = ""
            self.textBrowser_6.image = None
            self.textBrowser_6.price = ""
            self.textBrowser_6.colors = ""
        try:
            self.textBrowser_7.setText(self.NameList[6]["title"])
            self.textBrowser_7.Name = self.NameList[6]["title"]
            self.textBrowser_7.url = self.NameList[6]["href"]
            self.textBrowser_7.image = "https:"+self.NameList[6]["image"]
            self.textBrowser_7.price = self.NameList[6]["price"]
            self.textBrowser_7.colors = self.NameList[6]["colors"]
        except:
            self.textBrowser_7.setText("")
            self.textBrowser_7.Name = ""
            self.textBrowser_7.url = ""
            self.textBrowser_7.image = None
            self.textBrowser_7.price = ""
            self.textBrowser_7.colors = ""
        try:
            self.textBrowser_8.setText(self.NameList[7]["title"])
            self.textBrowser_8.Name = self.NameList[7]["title"]
            self.textBrowser_8.url = self.NameList[7]["href"]
            self.textBrowser_8.image = "https:"+self.NameList[7]["image"]
            self.textBrowser_8.price = self.NameList[7]["price"]
            self.textBrowser_8.colors = self.NameList[7]["colors"]
        except:
            self.textBrowser_8.setText("")
            self.textBrowser_8.Name = ""
            self.textBrowser_8.url = ""
            self.textBrowser_8.image = None
            self.textBrowser_8.price = ""
            self.textBrowser_8.colors = ""
        try:
            self.textBrowser_9.setText(self.NameList[8]["title"])
            self.textBrowser_9.Name = self.NameList[8]["title"]
            self.textBrowser_9.url = self.NameList[8]["href"]
            self.textBrowser_9.image = "https:"+self.NameList[8]["image"]
            self.textBrowser_9.price = self.NameList[8]["price"]
            self.textBrowser_9.colors = self.NameList[8]["colors"]
        except:
            self.textBrowser_9.setText("")
            self.textBrowser_9.Name = ""
            self.textBrowser_9.url = ""
            self.textBrowser_9.image = None
            self.textBrowser_9.price = ""
            self.textBrowser_9.colors = ""
        try:
            self.textBrowser_10.setText(self.NameList[9]["title"])
            self.textBrowser_10.Name = self.NameList[9]["title"]
            self.textBrowser_10.url = self.NameList[9]["href"]
            self.textBrowser_10.image = "https:"+self.NameList[9]["image"]
            self.textBrowser_10.price = self.NameList[9]["price"]
            self.textBrowser_10.colors = self.NameList[9]["colors"]
        except:
            self.textBrowser_10.setText("")
            self.textBrowser_10.Name = ""
            self.textBrowser_10.url = ""
            self.textBrowser_10.image = None
            self.textBrowser_10.price = ""
            self.textBrowser_10.colors = ""
        try:
            self.textBrowser_11.setText(self.NameList[10]["title"])
            self.textBrowser_11.Name = self.NameList[10]["title"]
            self.textBrowser_11.url = self.NameList[10]["href"]
            self.textBrowser_11.image = "https:"+self.NameList[10]["image"]
            self.textBrowser_11.price = self.NameList[10]["price"]
            self.textBrowser_11.colors = self.NameList[10]["colors"]
        except:
            self.textBrowser_11.setText("")
            self.textBrowser_11.Name = ""
            self.textBrowser_11.url = ""
            self.textBrowser_11.image = None
            self.textBrowser_11.price = ""
            self.textBrowser_11.colors = ""
        try:
            self.textBrowser_12.setText(self.NameList[11]["title"])
            self.textBrowser_12.Name = self.NameList[11]["title"]
            self.textBrowser_12.url = self.NameList[11]["href"]
            self.textBrowser_12.image = "https:"+self.NameList[11]["image"]
            self.textBrowser_12.price = self.NameList[11]["price"]
            self.textBrowser_12.colors = self.NameList[11]["colors"]
        except:
            self.textBrowser_12.setText("")
            self.textBrowser_12.Name = ""
            self.textBrowser_12.url = ""
            self.textBrowser_12.image = None
            self.textBrowser_12.price = ""
            self.textBrowser_12.colors = ""
        try:
            self.textBrowser_13.setText(self.NameList[12]["title"])
            self.textBrowser_13.Name = self.NameList[12]["title"]
            self.textBrowser_13.url = self.NameList[12]["href"]
            self.textBrowser_13.image = "https:"+self.NameList[12]["image"]
            self.textBrowser_13.price = self.NameList[12]["price"]
            self.textBrowser_13.colors = self.NameList[12]["colors"]
        except:
            self.textBrowser_13.setText("")
            self.textBrowser_13.Name = ""
            self.textBrowser_13.url = ""
            self.textBrowser_13.image = None
            self.textBrowser_13.price = ""
            self.textBrowser_13.colors = ""
        try:
            self.textBrowser_14.setText(self.NameList[13]["title"])
            self.textBrowser_14.Name = self.NameList[13]["title"]
            self.textBrowser_14.url = self.NameList[13]["href"]
            self.textBrowser_14.image = "https:"+self.NameList[13]["image"]
            self.textBrowser_14.price = self.NameList[13]["price"]
            self.textBrowser_14.colors = self.NameList[13]["colors"]
        except:
            self.textBrowser_14.setText("")
            self.textBrowser_14.Name = ""
            self.textBrowser_14.url = ""
            self.textBrowser_14.image = None
            self.textBrowser_14.price = ""
            self.textBrowser_14.colors = ""
        try:
            self.textBrowser_15.setText(self.NameList[14]["title"])
            self.textBrowser_15.Name = self.NameList[14]["title"]
            self.textBrowser_15.url = self.NameList[14]["href"]
            self.textBrowser_15.image = "https:"+self.NameList[14]["image"]
            self.textBrowser_15.price = self.NameList[14]["price"]
            self.textBrowser_15.colors = self.NameList[14]["colors"]
        except:
            self.textBrowser_15.setText("")
            self.textBrowser_15.Name = ""
            self.textBrowser_15.url = ""
            self.textBrowser_15.image = None
            self.textBrowser_15.price = ""
            self.textBrowser_15.colors = ""
        try:
            self.textBrowser_16.setText(self.NameList[15]["title"])
            self.textBrowser_16.Name = self.NameList[15]["title"]
            self.textBrowser_16.url = self.NameList[15]["href"]
            self.textBrowser_16.image = "https:"+self.NameList[15]["image"]
            self.textBrowser_16.price = self.NameList[15]["price"]
            self.textBrowser_16.colors = self.NameList[15]["colors"]
        except:
            self.textBrowser_16.setText("")
            self.textBrowser_16.Name = ""
            self.textBrowser_16.url = ""
            self.textBrowser_16.image = None
            self.textBrowser_16.price = ""
            self.textBrowser_16.colors = ""
        try:
            self.textBrowser_17.setText(self.NameList[16]["title"])
            self.textBrowser_17.Name = self.NameList[16]["title"]
            self.textBrowser_17.url = self.NameList[16]["href"]
            self.textBrowser_17.image = "https:"+self.NameList[16]["image"]
            self.textBrowser_17.price = self.NameList[16]["price"]
            self.textBrowser_17.colors = self.NameList[16]["colors"]
        except:
            self.textBrowser_17.setText("")
            self.textBrowser_17.Name = ""
            self.textBrowser_17.url = ""
            self.textBrowser_17.image = None
            self.textBrowser_17.price = ""
            self.textBrowser_17.colors = ""
        try:
            self.textBrowser_18.setText(self.NameList[17]["title"])
            self.textBrowser_18.Name = self.NameList[17]["title"]
            self.textBrowser_18.url = self.NameList[17]["href"]
            self.textBrowser_18.image = "https:"+self.NameList[17]["image"]
            self.textBrowser_18.price = self.NameList[17]["price"]
            self.textBrowser_18.colors = self.NameList[17]["colors"]
        except:
            self.textBrowser_18.setText("")
            self.textBrowser_18.Name = ""
            self.textBrowser_18.url = ""
            self.textBrowser_18.image = None
            self.textBrowser_18.price = ""
            self.textBrowser_18.colors = ""
        try:
            self.textBrowser_19.setText(self.NameList[18]["title"])
            self.textBrowser_19.Name = self.NameList[18]["title"]
            self.textBrowser_19.url = self.NameList[18]["href"]
            self.textBrowser_19.image = "https:"+self.NameList[18]["image"]
            self.textBrowser_19.price = self.NameList[18]["price"]
            self.textBrowser_19.colors = self.NameList[18]["colors"]
        except:
            self.textBrowser_19.setText("")
            self.textBrowser_19.Name = ""
            self.textBrowser_19.url = ""
            self.textBrowser_19.image = None
            self.textBrowser_19.price = ""
            self.textBrowser_19.colors = ""
        try:
            self.textBrowser_20.setText(self.NameList[19]["title"])
            self.textBrowser_20.Name = self.NameList[19]["title"]
            self.textBrowser_20.url = self.NameList[19]["href"]
            self.textBrowser_20.image = "https:"+self.NameList[19]["image"]
            self.textBrowser_20.price = self.NameList[19]["price"]
            self.textBrowser_20.colors = self.NameList[19]["colors"]
        except:
            self.textBrowser_20.setText("")
            self.textBrowser_20.Name = ""
            self.textBrowser_20.url = ""
            self.textBrowser_20.image = None
            self.textBrowser_20.price = ""
            self.textBrowser_20.colors = ""
        try:
            self.textBrowser_21.setText(self.NameList[20]["title"])
            self.textBrowser_21.Name = self.NameList[20]["title"]
            self.textBrowser_21.url = self.NameList[20]["href"]
            self.textBrowser_21.image = "https:"+self.NameList[20]["image"]
            self.textBrowser_21.price = self.NameList[20]["price"]
            self.textBrowser_21.colors = self.NameList[20]["colors"]
        except:
            self.textBrowser_21.setText("")
            self.textBrowser_21.Name = ""
            self.textBrowser_21.url = ""
            self.textBrowser_21.image = None
            self.textBrowser_21.price = ""
            self.textBrowser_21.colors = ""
        try:
            self.textBrowser_22.setText(self.NameList[21]["title"])
            self.textBrowser_22.Name = self.NameList[21]["title"]
            self.textBrowser_22.url = self.NameList[21]["href"]
            self.textBrowser_22.image = "https:"+self.NameList[21]["image"]
            self.textBrowser_22.price = self.NameList[21]["price"]
            self.textBrowser_22.colors = self.NameList[21]["colors"]
        except:
            self.textBrowser_22.setText("")
            self.textBrowser_22.Name = ""
            self.textBrowser_22.url = ""
            self.textBrowser_22.image = None
            self.textBrowser_22.price = ""
            self.textBrowser_22.colors = ""
        try:
            self.textBrowser_23.setText(self.NameList[22]["title"])
            self.textBrowser_23.Name = self.NameList[22]["title"]
            self.textBrowser_23.url = self.NameList[22]["href"]
            self.textBrowser_23.image = "https:"+self.NameList[22]["image"]
            self.textBrowser_23.price = self.NameList[22]["price"]
            self.textBrowser_23.colors = self.NameList[22]["colors"]
        except:
            self.textBrowser_23.setText("")
            self.textBrowser_23.Name = ""
            self.textBrowser_23.url = ""
            self.textBrowser_23.image = None
            self.textBrowser_23.price = ""
            self.textBrowser_23.colors = ""

#region ListClick Functionality
        self.textBrowser_1.clicked.connect(self.Button1Clk)
        self.textBrowser_2.clicked.connect(self.Button2Clk)
        self.textBrowser_3.clicked.connect(self.Button3Clk)
        self.textBrowser_4.clicked.connect(self.Button4Clk)
        self.textBrowser_5.clicked.connect(self.Button5Clk)
        self.textBrowser_6.clicked.connect(self.Button6Clk)
        self.textBrowser_7.clicked.connect(self.Button7Clk)
        self.textBrowser_8.clicked.connect(self.Button8Clk)
        self.textBrowser_9.clicked.connect(self.Button9Clk)
        self.textBrowser_10.clicked.connect(self.Button10Clk)
        self.textBrowser_11.clicked.connect(self.Button11Clk)
        self.textBrowser_12.clicked.connect(self.Button12Clk)
        self.textBrowser_13.clicked.connect(self.Button13Clk)
        self.textBrowser_14.clicked.connect(self.Button14Clk)
        self.textBrowser_15.clicked.connect(self.Button15Clk)
        self.textBrowser_16.clicked.connect(self.Button16Clk)
        self.textBrowser_17.clicked.connect(self.Button17Clk)
        self.textBrowser_18.clicked.connect(self.Button18Clk)
        self.textBrowser_19.clicked.connect(self.Button19Clk)
        self.textBrowser_20.clicked.connect(self.Button20Clk)
        self.textBrowser_21.clicked.connect(self.Button21Clk)
        self.textBrowser_22.clicked.connect(self.Button22Clk)
        self.textBrowser_23.clicked.connect(self.Button23Clk)
#endregion
#region List Button Click
    def Button1Clk(self):
        try:
            self.Name = self.textBrowser_1.Name
            self.url = self.textBrowser_1.url
            self.image = self.textBrowser_1.image
            self.colors = self.textBrowser_1.colors
            self.price = self.textBrowser_1.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button2Clk(self):
        try:
            self.Name = self.textBrowser_2.Name
            self.url = self.textBrowser_2.url
            self.image = self.textBrowser_2.image
            self.colors = self.textBrowser_2.colors
            self.price = self.textBrowser_2.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button3Clk(self):
        try:
            self.Name = self.textBrowser_3.Name
            self.url = self.textBrowser_3.url
            self.image = self.textBrowser_3.image
            self.colors = self.textBrowser_3.colors
            self.price = self.textBrowser_3.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button4Clk(self):
        try:
            self.Name = self.textBrowser_4.Name
            self.url = self.textBrowser_4.url
            self.image = self.textBrowser_4.image
            self.colors = self.textBrowser_4.colors
            self.price = self.textBrowser_4.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button5Clk(self):
        try:
            self.Name = self.textBrowser_5.Name
            self.url = self.textBrowser_5.url
            self.image = self.textBrowser_5.image
            self.colors = self.textBrowser_5.colors
            self.price = self.textBrowser_5.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button6Clk(self):
        try:
            self.Name = self.textBrowser_6.Name
            self.url = self.textBrowser_6.url
            self.image = self.textBrowser_6.image
            self.colors = self.textBrowser_6.colors
            self.price = self.textBrowser_6.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button7Clk(self):
        try:
            self.Name = self.textBrowser_7.Name
            self.url = self.textBrowser_7.url
            self.image = self.textBrowser_7.image
            self.colors = self.textBrowser_7.colors
            self.price = self.textBrowser_7.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button8Clk(self):
        try:
            self.Name = self.textBrowser_8.Name
            self.url = self.textBrowser_8.url
            self.image = self.textBrowser_8.image
            self.colors = self.textBrowser_8.colors
            self.price = self.textBrowser_8.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button9Clk(self):
        try:
            self.Name = self.textBrowser_9.Name
            self.url = self.textBrowser_9.url
            self.image = self.textBrowser_9.image
            self.colors = self.textBrowser_9.colors
            self.price = self.textBrowser_9.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button10Clk(self):
        try:
            self.Name = self.textBrowser_10.Name
            self.url = self.textBrowser_10.url
            self.image = self.textBrowser_10.image
            self.colors = self.textBrowser_10.colors
            self.price = self.textBrowser_10.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button11Clk(self):
        try:
            self.Name = self.textBrowser_11.Name
            self.url = self.textBrowser_11.url
            self.image = self.textBrowser_11.image
            self.colors = self.textBrowser_11.colors
            self.price = self.textBrowser_11.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button12Clk(self):
        try:
            self.Name = self.textBrowser_12.Name
            self.url = self.textBrowser_12.url
            self.image = self.textBrowser_12.image
            self.colors = self.textBrowser_12.colors
            self.price = self.textBrowser_12.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button13Clk(self):
        try:
            self.Name = self.textBrowser_13.Name
            self.url = self.textBrowser_13.url
            self.image = self.textBrowser_13.image
            self.colors = self.textBrowser_13.colors
            self.price = self.textBrowser_13.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button14Clk(self):
        try:
            self.Name = self.textBrowser_14.Name
            self.url = self.textBrowser_14.url
            self.image = self.textBrowser_14.image
            self.colors = self.textBrowser_14.colors
            self.price = self.textBrowser_14.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button15Clk(self):
        try:
            self.Name = self.textBrowser_15.Name
            self.url = self.textBrowser_15.url
            self.image = self.textBrowser_15.image
            self.colors = self.textBrowser_15.colors
            self.price = self.textBrowser_15.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button16Clk(self):
        try:
            self.Name = self.textBrowser_16.Name
            self.url = self.textBrowser_16.url
            self.image = self.textBrowser_16.image
            self.colors = self.textBrowser_16.colors
            self.price = self.textBrowser_16.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button17Clk(self):
        try:
            self.Name = self.textBrowser_17.Name
            self.url = self.textBrowser_17.url
            self.image = self.textBrowser_17.image
            self.colors = self.textBrowser_17.colors
            self.price = self.textBrowser_17.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button18Clk(self):
        try:
            self.Name = self.textBrowser_18.Name
            self.url = self.textBrowser_18.url
            self.image = self.textBrowser_18.image
            self.colors = self.textBrowser_18.colors
            self.price = self.textBrowser_18.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button19Clk(self):
        try:
            self.Name = self.textBrowser_19.Name
            self.url = self.textBrowser_19.url
            self.image = self.textBrowser_19.image
            self.colors = self.textBrowser_19.colors
            self.price = self.textBrowser_19.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button20Clk(self):
        try:
            self.Name = self.textBrowser_20.Name
            self.url = self.textBrowser_20.url
            self.image = self.textBrowser_20.image
            self.colors = self.textBrowser_20.colors
            self.price = self.textBrowser_20.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button21Clk(self):
        try:
            self.Name = self.textBrowser_21.Name
            self.url = self.textBrowser_21.url
            self.image = self.textBrowser_21.image
            self.colors = self.textBrowser_21.colors
            self.price = self.textBrowser_21.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button22Clk(self):
        try:
            self.Name = self.textBrowser_22.Name
            self.url = self.textBrowser_22.url
            self.image = self.textBrowser_22.image
            self.colors = self.textBrowser_22.colors
            self.price = self.textBrowser_22.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()
    def Button23Clk(self):
        try:
            self.Name = self.textBrowser_23.Name
            self.url = self.textBrowser_23.url
            self.image = self.textBrowser_23.image
            self.colors = self.textBrowser_23.colors
            self.price = self.textBrowser_23.price
            self.NameRefresh()
        except:
            self.Name = ""
            self.url = ""
            self.image = None
            self.price = ""
            self.colors = ""
            self.price = ""
            self.NameRefresh()   
#endregion
#endregion
#region HIDE
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Name:"))
        # self.label_2.setText(_translate("MainWindow", "Nike Air Force 1 \'07"))
        self.label_7.setText(_translate("MainWindow", "Colors:"))
        # self.label_8.setText(_translate("MainWindow", "Blue, Red"))
        self.label_4.setText(_translate("MainWindow", "Price:"))
        # self.label_6.setText(_translate("MainWindow", "100.00$"))
        self.label_5.setText(_translate("MainWindow", "Link:"))
        # self.pushButton.setText(_translate("MainWindow", "www.Google.com"))
        self.OKBtn.setText(_translate("MainWindow", "OK"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "search"))
        self.backBtn.setText(_translate("MainWindow", "Menu"))
        self.pushButton_2.setText(_translate("MainWindow", "UPARROW"))
        self.pushButton_3.setText(_translate("MainWindow", "DOWNARROW"))
        self.pushButton_3.clicked.connect(self.arrowdown)
        self.pushButton_2.clicked.connect(self.arrowup)
        self.pushButton.clicked.connect(self.URLOPEN)
        self.OKBtn.clicked.connect(self.SearchButtonClicked)
    def NameRefresh(self):
        if self.image == None:
            self.ItemIMG.setPixmap(self.defaultpixmap)
        else:
            self.pixmap = QPixmap()
            self.pixmap.loadFromData(PicRequest(self.image))
            self.ItemIMG.setPixmap(self.pixmap)
        self.label_2.setText(self.Name)
        self.label_6.setText(self.price)
        self.pushButton.setText(self.url)
        self.label_8.setText(self.colors)
    def arrowdown(self):
        if self.value+23 < len(self.NameList):
            self.value=self.value+1
            for index,item in enumerate(self.textBrowserGroup):
                item.setText(self.NameList[index+self.value]["title"])
                item.Name = self.NameList[index+self.value]["title"]
                item.url = self.NameList[index+self.value]["href"]
                item.image = "https:"+self.NameList[index+self.value]["image"]
                item.colors = self.NameList[index+self.value]["colors"]
                item.price = self.NameList[index+self.value]["price"]
    def arrowup(self):
        if self.value > 0:
            self.value=self.value-1
            for index,item in enumerate(self.textBrowserGroup):
                item.setText(self.NameList[index+self.value]["title"])
                item.Name = self.NameList[index+self.value]["title"]
                item.url = self.NameList[index+self.value]["href"]
                item.image = "https:"+self.NameList[index+self.value]["image"]
                item.colors = self.NameList[index+self.value]["colors"]
                item.price = self.NameList[index+self.value]["price"]
    def URLOPEN(self):
        webbrowser.open(self.url, new=0)
    def openWindow(self, MainWindow, inputtext):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window, db=self.db, catagory=self.catagory, search=inputtext)
        MainWindow.hide()
        self.window.show()
    def SearchButtonClicked(self):
        self.openWindow(self.MainWindow, self.lineEdit.text())
    def BckButtonClicked(self):
        self.MainWindow.hide()
        self.MenuBASE = QtWidgets.QWidget()
        self.MenuUI = Menu.Ui_Widget()
        self.MenuUI.setupUi(self.MenuBASE)
        self.MenuBASE.show()
#endregion
#endregion