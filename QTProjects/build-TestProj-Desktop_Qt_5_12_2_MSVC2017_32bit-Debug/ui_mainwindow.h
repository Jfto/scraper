/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QWidget *widget;
    QLabel *label;
    QLabel *label_4;
    QPushButton *pushButton;
    QPushButton *OKBtn;
    QLineEdit *lineEdit;
    QTextBrowser *textBrowser_15;
    QTextBrowser *textBrowser_20;
    QTextBrowser *textBrowser_17;
    QTextBrowser *textBrowser_12;
    QTextBrowser *textBrowser_10;
    QTextBrowser *textBrowser_9;
    QTextBrowser *textBrowser_22;
    QTextBrowser *textBrowser_19;
    QTextBrowser *textBrowser_7;
    QTextBrowser *textBrowser_8;
    QTextBrowser *textBrowser;
    QTextBrowser *textBrowser_23;
    QTextBrowser *textBrowser_14;
    QTextBrowser *textBrowser_6;
    QTextBrowser *textBrowser_11;
    QTextBrowser *textBrowser_18;
    QTextBrowser *textBrowser_13;
    QTextBrowser *textBrowser_2;
    QTextBrowser *textBrowser_5;
    QTextBrowser *textBrowser_21;
    QTextBrowser *textBrowser_4;
    QTextBrowser *textBrowser_3;
    QTextBrowser *textBrowser_16;
    QPushButton *backBtn;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QLabel *ItemIMG;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(721, 563);
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        MainWindow->setBaseSize(QSize(721, 517));
        MainWindow->setStyleSheet(QString::fromUtf8("border: 1px solid black"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        widget = new QWidget(centralWidget);
        widget->setObjectName(QString::fromUtf8("widget"));
        widget->setGeometry(QRect(430, 250, 261, 271));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(widget->sizePolicy().hasHeightForWidth());
        widget->setSizePolicy(sizePolicy1);
        widget->setBaseSize(QSize(261, 271));
        widget->setAutoFillBackground(false);
        widget->setStyleSheet(QString::fromUtf8("background-color: white;\n"
"border: 1px solid grey;"));
        label = new QLabel(widget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(10, 10, 47, 13));
        label->setStyleSheet(QString::fromUtf8("border: 0px"));
        label->setLineWidth(0);
        label_4 = new QLabel(widget);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(10, 70, 47, 13));
        label_4->setStyleSheet(QString::fromUtf8("border: 0px"));
        label_4->setLineWidth(0);
        pushButton = new QPushButton(widget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(50, 70, 75, 23));
        pushButton->setStyleSheet(QString::fromUtf8("border: 0px; color: \"dark blue\"; text-decoration: underline;"));
        OKBtn = new QPushButton(centralWidget);
        OKBtn->setObjectName(QString::fromUtf8("OKBtn"));
        OKBtn->setGeometry(QRect(350, 5, 41, 21));
        sizePolicy1.setHeightForWidth(OKBtn->sizePolicy().hasHeightForWidth());
        OKBtn->setSizePolicy(sizePolicy1);
        OKBtn->setBaseSize(QSize(41, 21));
        lineEdit = new QLineEdit(centralWidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(19, 6, 327, 21));
        sizePolicy1.setHeightForWidth(lineEdit->sizePolicy().hasHeightForWidth());
        lineEdit->setSizePolicy(sizePolicy1);
        lineEdit->setBaseSize(QSize(327, 21));
        lineEdit->setStyleSheet(QString::fromUtf8("background-color: white;\n"
"border: 1px solid grey;"));
        lineEdit->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        textBrowser_15 = new QTextBrowser(centralWidget);
        textBrowser_15->setObjectName(QString::fromUtf8("textBrowser_15"));
        textBrowser_15->setGeometry(QRect(20, 360, 371, 21));
        textBrowser_15->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_15->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_15->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_20 = new QTextBrowser(centralWidget);
        textBrowser_20->setObjectName(QString::fromUtf8("textBrowser_20"));
        textBrowser_20->setGeometry(QRect(20, 420, 371, 21));
        textBrowser_20->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_20->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_20->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_17 = new QTextBrowser(centralWidget);
        textBrowser_17->setObjectName(QString::fromUtf8("textBrowser_17"));
        textBrowser_17->setGeometry(QRect(20, 400, 371, 21));
        textBrowser_17->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_17->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_17->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_12 = new QTextBrowser(centralWidget);
        textBrowser_12->setObjectName(QString::fromUtf8("textBrowser_12"));
        textBrowser_12->setGeometry(QRect(20, 260, 371, 21));
        textBrowser_12->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_12->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_12->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_10 = new QTextBrowser(centralWidget);
        textBrowser_10->setObjectName(QString::fromUtf8("textBrowser_10"));
        textBrowser_10->setGeometry(QRect(20, 220, 371, 21));
        textBrowser_10->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_10->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_10->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_9 = new QTextBrowser(centralWidget);
        textBrowser_9->setObjectName(QString::fromUtf8("textBrowser_9"));
        textBrowser_9->setGeometry(QRect(20, 240, 371, 21));
        textBrowser_9->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_9->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_9->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_22 = new QTextBrowser(centralWidget);
        textBrowser_22->setObjectName(QString::fromUtf8("textBrowser_22"));
        textBrowser_22->setGeometry(QRect(20, 480, 371, 21));
        textBrowser_22->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_22->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_22->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_19 = new QTextBrowser(centralWidget);
        textBrowser_19->setObjectName(QString::fromUtf8("textBrowser_19"));
        textBrowser_19->setGeometry(QRect(20, 440, 371, 21));
        textBrowser_19->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_19->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_19->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_7 = new QTextBrowser(centralWidget);
        textBrowser_7->setObjectName(QString::fromUtf8("textBrowser_7"));
        textBrowser_7->setGeometry(QRect(20, 200, 371, 21));
        textBrowser_7->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_7->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_7->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_8 = new QTextBrowser(centralWidget);
        textBrowser_8->setObjectName(QString::fromUtf8("textBrowser_8"));
        textBrowser_8->setGeometry(QRect(20, 180, 371, 21));
        textBrowser_8->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_8->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_8->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser = new QTextBrowser(centralWidget);
        textBrowser->setObjectName(QString::fromUtf8("textBrowser"));
        textBrowser->setGeometry(QRect(20, 60, 371, 21));
        textBrowser->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_23 = new QTextBrowser(centralWidget);
        textBrowser_23->setObjectName(QString::fromUtf8("textBrowser_23"));
        textBrowser_23->setGeometry(QRect(20, 500, 371, 21));
        textBrowser_23->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_23->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_23->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_14 = new QTextBrowser(centralWidget);
        textBrowser_14->setObjectName(QString::fromUtf8("textBrowser_14"));
        textBrowser_14->setGeometry(QRect(20, 300, 371, 21));
        textBrowser_14->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_14->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_14->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_6 = new QTextBrowser(centralWidget);
        textBrowser_6->setObjectName(QString::fromUtf8("textBrowser_6"));
        textBrowser_6->setGeometry(QRect(20, 140, 371, 21));
        textBrowser_6->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_6->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_6->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_11 = new QTextBrowser(centralWidget);
        textBrowser_11->setObjectName(QString::fromUtf8("textBrowser_11"));
        textBrowser_11->setGeometry(QRect(20, 280, 371, 21));
        textBrowser_11->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_11->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_11->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_18 = new QTextBrowser(centralWidget);
        textBrowser_18->setObjectName(QString::fromUtf8("textBrowser_18"));
        textBrowser_18->setGeometry(QRect(20, 380, 371, 21));
        textBrowser_18->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_18->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_18->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_13 = new QTextBrowser(centralWidget);
        textBrowser_13->setObjectName(QString::fromUtf8("textBrowser_13"));
        textBrowser_13->setGeometry(QRect(20, 320, 371, 21));
        textBrowser_13->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_13->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_13->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_2 = new QTextBrowser(centralWidget);
        textBrowser_2->setObjectName(QString::fromUtf8("textBrowser_2"));
        textBrowser_2->setGeometry(QRect(20, 80, 371, 21));
        textBrowser_2->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_2->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_2->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_5 = new QTextBrowser(centralWidget);
        textBrowser_5->setObjectName(QString::fromUtf8("textBrowser_5"));
        textBrowser_5->setGeometry(QRect(20, 160, 371, 21));
        textBrowser_5->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_5->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_5->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_21 = new QTextBrowser(centralWidget);
        textBrowser_21->setObjectName(QString::fromUtf8("textBrowser_21"));
        textBrowser_21->setGeometry(QRect(20, 460, 371, 21));
        textBrowser_21->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_21->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_21->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_4 = new QTextBrowser(centralWidget);
        textBrowser_4->setObjectName(QString::fromUtf8("textBrowser_4"));
        textBrowser_4->setGeometry(QRect(20, 100, 371, 21));
        textBrowser_4->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_4->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_4->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_3 = new QTextBrowser(centralWidget);
        textBrowser_3->setObjectName(QString::fromUtf8("textBrowser_3"));
        textBrowser_3->setGeometry(QRect(20, 120, 371, 21));
        textBrowser_3->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_3->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_3->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_16 = new QTextBrowser(centralWidget);
        textBrowser_16->setObjectName(QString::fromUtf8("textBrowser_16"));
        textBrowser_16->setGeometry(QRect(20, 340, 371, 21));
        textBrowser_16->setStyleSheet(QString::fromUtf8("border: 1px solid grey;"));
        textBrowser_16->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textBrowser_16->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        backBtn = new QPushButton(centralWidget);
        backBtn->setObjectName(QString::fromUtf8("backBtn"));
        backBtn->setGeometry(QRect(640, 10, 51, 21));
        pushButton_2 = new QPushButton(centralWidget);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setGeometry(QRect(170, 36, 80, 20));
        pushButton_3 = new QPushButton(centralWidget);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        pushButton_3->setGeometry(QRect(170, 530, 80, 21));
        ItemIMG = new QLabel(centralWidget);
        ItemIMG->setObjectName(QString::fromUtf8("ItemIMG"));
        ItemIMG->setGeometry(QRect(430, 60, 261, 181));
        ItemIMG->setStyleSheet(QString::fromUtf8("background-image: url(\"https://ichef.bbci.co.uk/news/976/cpsprodpb/27C9/production/_103158101_tha.jpg\");"));
        ItemIMG->setScaledContents(true);
        MainWindow->setCentralWidget(centralWidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        label->setText(QApplication::translate("MainWindow", "Name:", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "Name:", nullptr));
        pushButton->setText(QApplication::translate("MainWindow", "PushButton", nullptr));
        OKBtn->setText(QApplication::translate("MainWindow", "OK", nullptr));
        lineEdit->setPlaceholderText(QApplication::translate("MainWindow", "search", nullptr));
        backBtn->setText(QApplication::translate("MainWindow", "Menu", nullptr));
        pushButton_2->setText(QApplication::translate("MainWindow", "UPARROW", nullptr));
        pushButton_3->setText(QApplication::translate("MainWindow", "DOWNARROW", nullptr));
        ItemIMG->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
