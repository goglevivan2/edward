# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui//decryptor.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Message Decoder")
        MainWindow.resize(303, 347)
        MainWindow.setStyleSheet("QPushButton{\n"
"text-align: center;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:silver;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:gray;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_message = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_message.setGeometry(QtCore.QRect(20, 60, 261, 131))
        self.textBrowser_message.setObjectName("textBrowser_message")
        self.pushButton_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decrypt.setGeometry(QtCore.QRect(20, 200, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        self.pushButton_decrypt.setFont(font)
        self.pushButton_decrypt.setStyleSheet("")
        self.pushButton_decrypt.setObjectName("pushButton_decrypt")
        self.lineEdit_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_path.setGeometry(QtCore.QRect(20, 20, 261, 31))
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(20, 260, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_decrypt.setText(_translate("MainWindow", "decrypt file"))
        self.lineEdit_path.setPlaceholderText(_translate("MainWindow", "enter file path"))
        self.pushButton_clear.setText(_translate("MainWindow", "clear all"))