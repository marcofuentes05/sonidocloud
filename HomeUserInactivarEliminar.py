# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeUserInactivarEliminar.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeUserInactivarEliminar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 650))
        MainWindow.setStyleSheet("background-color: rgb(72,35,60);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 40, 900, 550))
        self.frame.setMinimumSize(QtCore.QSize(900, 550))
        self.frame.setMaximumSize(QtCore.QSize(900, 550))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 50, 205, 50))
        self.label.setMinimumSize(QtCore.QSize(205, 50))
        self.label.setMaximumSize(QtCore.QSize(205, 50))
        self.label.setStyleSheet("font: 24pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(609, 130, 230, 50))
        self.label_7.setMinimumSize(QtCore.QSize(220, 50))
        self.label_7.setMaximumSize(QtCore.QSize(230, 25))
        self.label_7.setStyleSheet("font: 19pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(609, 230, 262, 231))
        self.tableWidget.setStyleSheet("font: 13pt \"Times\";\n"
"color: rgb(64, 55, 110);\n"
"background-color: rgb(212, 228, 188);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.pushButton_Login = QtWidgets.QPushButton(self.frame)
        self.pushButton_Login.setGeometry(QtCore.QRect(756, 50, 114, 32))
        self.pushButton_Login.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_Login.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_Login.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.textEdit_UserBuscar = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(640, 200, 231, 31))
        self.textEdit_UserBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(609, 199, 31, 31))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("finder.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 130, 220, 50))
        self.label_8.setMinimumSize(QtCore.QSize(220, 50))
        self.label_8.setMaximumSize(QtCore.QSize(210, 25))
        self.label_8.setStyleSheet("font: 19pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 199, 31, 31))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("finder.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.textEdit_UserBuscar_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_UserBuscar_2.setGeometry(QtCore.QRect(61, 200, 231, 31))
        self.textEdit_UserBuscar_2.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit_UserBuscar_2.setObjectName("textEdit_UserBuscar_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 230, 262, 231))
        self.tableWidget_2.setStyleSheet("font: 13pt \"Times\";\n"
"color: rgb(64, 55, 110);\n"
"background-color: rgb(212, 228, 188);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.pushButton_Login_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Login_2.setGeometry(QtCore.QRect(104, 480, 114, 32))
        self.pushButton_Login_2.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_Login_2.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_Login_2.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Login_2.setObjectName("pushButton_Login_2")
        self.pushButton_Login_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Login_3.setGeometry(QtCore.QRect(683, 490, 114, 32))
        self.pushButton_Login_3.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_Login_3.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_Login_3.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Login_3.setObjectName("pushButton_Login_3")
        self.label_8.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tableWidget.raise_()
        self.pushButton_Login.raise_()
        self.textEdit_UserBuscar.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.textEdit_UserBuscar_2.raise_()
        self.tableWidget_2.raise_()
        self.pushButton_Login_2.raise_()
        self.pushButton_Login_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
        self.label_7.setText(_translate("MainWindow", "Inactivación de Canción"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "aqui"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "van"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "las"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "filas"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "proyecto"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "canciones"))
        self.pushButton_Login.setText(_translate("MainWindow", "Exit"))
        self.textEdit_UserBuscar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Eliminación de Canción"))
        self.textEdit_UserBuscar_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "aqui"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "van"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "las"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "filas"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "proyecto"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "canciones"))
        self.pushButton_Login_2.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_Login_3.setText(_translate("MainWindow", "Inactivar"))