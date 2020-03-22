# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeUserAuto.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from HomeUserInactivarEliminar import Ui_HomeUserInactivarEliminar
from HomeUserModificar import Ui_HomeUserModificar
from HomeUserRegistrar import Ui_HomeUserRegistrar


class Ui_HomeUserAuto(object):
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
        self.label.setGeometry(QtCore.QRect(130, 40, 205, 50))
        self.label.setMinimumSize(QtCore.QSize(205, 50))
        self.label.setMaximumSize(QtCore.QSize(205, 50))
        self.label.setStyleSheet("font: 24pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 130, 230, 25))
        self.label_7.setMinimumSize(QtCore.QSize(230, 25))
        self.label_7.setMaximumSize(QtCore.QSize(230, 25))
        self.label_7.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(30, 260, 841, 261))
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
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(640, 230, 231, 31))
        self.textEdit_UserBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(609, 229, 31, 31))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("finder.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_Registro = QtWidgets.QPushButton(self.frame)
        self.pushButton_Registro.setGeometry(QtCore.QRect(30, 150, 114, 30))
        self.pushButton_Registro.setMinimumSize(QtCore.QSize(114, 30))
        self.pushButton_Registro.setMaximumSize(QtCore.QSize(114, 30))
        self.pushButton_Registro.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Registro.setObjectName("pushButton_Registro")
        self.pushButton_Registro.clicked.connect(self.openHomeUserRegistrar)
        self.pushButton_Inactivar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Inactivar.setGeometry(QtCore.QRect(272, 150, 114, 30))
        self.pushButton_Inactivar.setMinimumSize(QtCore.QSize(114, 30))
        self.pushButton_Inactivar.setMaximumSize(QtCore.QSize(114, 30))
        self.pushButton_Inactivar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Inactivar.setObjectName("pushButton_Inactivar")
        self.pushButton_Inactivar.clicked.connect(self.openHomeUserInactivarEliminar)
        self.pushButton_Modficiar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Modficiar.setGeometry(QtCore.QRect(514, 150, 114, 30))
        self.pushButton_Modficiar.setMinimumSize(QtCore.QSize(114, 30))
        self.pushButton_Modficiar.setMaximumSize(QtCore.QSize(114, 30))
        self.pushButton_Modficiar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Modficiar.setObjectName("pushButton_Modficiar")
        self.pushButton_Modficiar.clicked.connect(self.openHomeUserModificar)
        self.pushButton_Eliminar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Eliminar.setGeometry(QtCore.QRect(757, 150, 114, 30))
        self.pushButton_Eliminar.setMinimumSize(QtCore.QSize(114, 30))
        self.pushButton_Eliminar.setMaximumSize(QtCore.QSize(114, 30))
        self.pushButton_Eliminar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Eliminar.setObjectName("pushButton_Eliminar")
        self.pushButton_Eliminar.clicked.connect(self.openHomeUserInactivarEliminar)
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tableWidget.raise_()
        self.pushButton_Exit.raise_()
        self.textEdit_UserBuscar.raise_()
        self.label_4.raise_()
        self.pushButton_Registro.raise_()
        self.pushButton_Inactivar.raise_()
        self.pushButton_Modficiar.raise_()
        self.pushButton_Eliminar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
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
        self.pushButton_Registro.setText(_translate("MainWindow", "Registro"))
        self.pushButton_Inactivar.setText(_translate("MainWindow", "Inactivación"))
        self.pushButton_Modficiar.setText(_translate("MainWindow", "Modificación"))
        self.pushButton_Eliminar.setText(_translate("MainWindow", "Eliminación"))


    def openHomeUserInactivarEliminar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeUserInactivarEliminar()
        self.ui.setupUi(self.window)
        self.window.show()


    def openHomeUserModificar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeUserModificar()
        self.ui.setupUi(self.window)
        self.window.show()

    def openHomeUserRegistrar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeUserRegistrar()
        self.ui.setupUi(self.window)
        self.window.show()


