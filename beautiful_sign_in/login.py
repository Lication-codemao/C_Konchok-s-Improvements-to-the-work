# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 653)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 340, 490))
        self.label.setStyleSheet("border-image: url(:/images/images/1.jpg);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 100, 421, 491))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(560, 140, 215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"    border:none;\n"
"}\n"
"#pushButton:focus{\n"
"    color: rgb(186, 186, 186);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    border:none;\n"
"}\n"
"#pushButton_2:focus{\n"
"    color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(470, 200, 391, 361))
        self.widget_2.setObjectName("widget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 150, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 260, 331, 51))
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border:3px solid rgb(0,0,0);\n"
"    border-radius:8px\n"
"}\n"
"#pushButton_3:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"#pushButton_3:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setGeometry(QtCore.QRect(30, 220, 71, 21))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(820, 120, 31, 31))
        self.pushButton_4.setStyleSheet("border:none;")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(470, 200, 391, 361))
        self.widget_3.setObjectName("widget_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 50, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 120, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 190, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 260, 331, 51))
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border:3px solid rgb(0,0,0);\n"
"    border-radius:8px\n"
"}\n"
"#pushButton_5:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"#pushButton_5:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(160, 260, 271, 151))
        self.widget_4.setObjectName("widget_4")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 261, 151))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:50px;\n"
"border-bottom-right-radius:50px;\n"
"border-top-left-radius:50px;\n"
"border-bottom-left-radius:50px;\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 110, 111, 31))
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border:3px solid rgb(0,0,0);\n"
"    border-radius:8px\n"
"}\n"
"#pushButton_6:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"#pushButton_6:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(120, 10, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setGeometry(QtCore.QRect(60, 50, 151, 31))
        self.label_5.setStyleSheet("font: 22pt \"??????\";")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.pushButton_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.pushButton_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "??????"))
        self.pushButton_2.setText(_translate("MainWindow", "??????"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "?????????"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "?????????"))
        self.pushButton_3.setText(_translate("MainWindow", "??????"))
        self.checkBox.setText(_translate("MainWindow", "?????????"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "???????????????"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "???????????????"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "???????????????"))
        self.pushButton_5.setText(_translate("MainWindow", "??????"))
        self.pushButton_6.setText(_translate("MainWindow", "OK"))
        self.label_4.setText(_translate("MainWindow", "??????"))
        self.label_5.setText(_translate("MainWindow", "????????????"))
import resource_rc
