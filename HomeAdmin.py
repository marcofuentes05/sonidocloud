# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi

class Ui_HomeAdmin(object):
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
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(:/newPrefix/WhatsApp Image 2020-03-16 at 9.47.22 PM.jpeg);")
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
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 210, 25))
        self.label_3.setMinimumSize(QtCore.QSize(210, 25))
        self.label_3.setMaximumSize(QtCore.QSize(210, 25))
        self.label_3.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(30, 150, 300, 30))
        self.comboBox.setMinimumSize(QtCore.QSize(300, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(300, 30))
        self.comboBox.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(640, 150, 230, 30))
        self.comboBox_2.setMinimumSize(QtCore.QSize(230, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(230, 30))
        self.comboBox_2.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(370, 150, 220, 30))
        self.comboBox_3.setMinimumSize(QtCore.QSize(220, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(220, 30))
        self.comboBox_3.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(370, 130, 210, 25))
        self.label_6.setMinimumSize(QtCore.QSize(210, 25))
        self.label_6.setMaximumSize(QtCore.QSize(210, 25))
        self.label_6.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(640, 130, 230, 25))
        self.label_7.setMinimumSize(QtCore.QSize(230, 25))
        self.label_7.setMaximumSize(QtCore.QSize(230, 25))
        self.label_7.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(30, 230, 841, 281))
        self.tableWidget.setStyleSheet("font: 13pt \"Times\";\n"
"color: rgb(64, 55, 110);\n"
"background-color: rgb(212, 228, 188);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButton_Exit = QtWidgets.QPushButton(self.frame)
        self.pushButton_Exit.setGeometry(QtCore.QRect(756, 50, 114, 32))
        self.pushButton_Exit.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_Exit.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_Exit.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.pushButton_Exit.clicked.connect(QtCore.QCoreApplication.instance().quit)
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
        self.label_7.raise_()
        self.label_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.comboBox_3.raise_()
        self.tableWidget.raise_()
        self.pushButton_Exit.raise_()
        self.textEdit_UserBuscar.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
        self.label_3.setText(_translate("MainWindow", "Módulo de reportería"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Reportería"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Artistas por área"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Géneros con más canciones"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Artistas con más albums individuales"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Canciones de mayor duración con la información de sus artistas"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Usuarios que han registrado más canciones"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Promedio de duración de canciones por género"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Álbumes más recientes"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Artistas más colaborativos"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Autorización"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Registros"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Inactivación"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Modificación"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Inactivación"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Búsquedas"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Canción"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Artista"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Álbum"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Género"))
        self.label_6.setText(_translate("MainWindow", "Módulo de búsquedas"))
        self.label_7.setText(_translate("MainWindow", "Módulo de autorización"))
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
        item.setText(_translate("MainWindow", "aqui"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "van"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "las"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "columnas"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "proyecto"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Exit"))
        self.textEdit_UserBuscar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))



    
    
