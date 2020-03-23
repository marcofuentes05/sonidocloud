# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import psycopg2 as bd
from PyQt5 import QtCore, QtGui, QtWidgets
from HomeUserInactivarEliminar import Ui_HomeUserInactivarEliminar
from HomeUserModificar import Ui_HomeUserModificar
from HomeUserRegistrar import Ui_HomeUserRegistrar


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
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 210, 25))
        self.label_3.setMinimumSize(QtCore.QSize(210, 25))
        self.label_3.setMaximumSize(QtCore.QSize(210, 25))
        self.label_3.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(30, 130, 201, 30))
        self.comboBox.setMinimumSize(QtCore.QSize(150, 30))
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
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 170, 230, 25))
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
        # self.tableWidget.setColumnCount(5)
        # self.tableWidget.setRowCount(6)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(4, item)
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
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(565, 230, 231, 31))
        self.textEdit_UserBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(534, 229, 31, 31))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("finder.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_Registro = QtWidgets.QPushButton(self.frame)
        self.pushButton_Registro.setGeometry(QtCore.QRect(30, 190, 114, 30))
        self.pushButton_Registro.setMinimumSize(QtCore.QSize(114, 30))
        self.pushButton_Registro.setMaximumSize(QtCore.QSize(114, 30))
        self.pushButton_Registro.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Registro.setObjectName("pushButton_Registro")
        self.pushButton_Registro.clicked.connect(self.openHomeUserRegistrar)
        self.pushButton_Inactivar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Inactivar.setGeometry(QtCore.QRect(272, 190, 114, 30))
        self.pushButton_Inactivar.setMinimumSize(QtCore.QSize(114, 30))
        self.pushButton_Inactivar.setMaximumSize(QtCore.QSize(114, 30))
        self.pushButton_Inactivar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Inactivar.setObjectName("pushButton_Inactivar")
        self.pushButton_Inactivar.clicked.connect(self.openHomeUserInactivarEliminar)
        self.pushButton_Modficiar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Modficiar.setGeometry(QtCore.QRect(514, 190, 114, 30))
        self.pushButton_Modficiar.setMinimumSize(QtCore.QSize(114, 30))
        self.pushButton_Modficiar.setMaximumSize(QtCore.QSize(114, 30))
        self.pushButton_Modficiar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Modficiar.setObjectName("pushButton_Modficiar")
        self.pushButton_Modficiar.clicked.connect(self.openHomeUserModificar)
        self.pushButton_Eliminar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Eliminar.setGeometry(QtCore.QRect(757, 190, 114, 30))
        self.pushButton_Eliminar.setMinimumSize(QtCore.QSize(114, 30))
        self.pushButton_Eliminar.setMaximumSize(QtCore.QSize(114, 30))
        self.pushButton_Eliminar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Eliminar.setObjectName("pushButton_Eliminar")
        self.pushButton_Eliminar.clicked.connect(self.openHomeUserInactivarEliminar)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(240, 110, 550, 25))
        self.label_5.setMinimumSize(QtCore.QSize(550, 25))
        self.label_5.setMaximumSize(QtCore.QSize(550, 25))
        self.label_5.setStyleSheet("font: 13pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_5.setObjectName("label_5")
        self.pushButton_Op1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Op1.setGeometry(QtCore.QRect(240, 130, 75, 30))
        self.pushButton_Op1.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_Op1.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Op1.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Op1.setObjectName("pushButton_Op1")
        self.pushButton_Op2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Op2.setGeometry(QtCore.QRect(319, 130, 75, 30))
        self.pushButton_Op2.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_Op2.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Op2.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Op2.setObjectName("pushButton_Op2")
        self.pushButton_Op4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Op4.setGeometry(QtCore.QRect(477, 130, 75, 30))
        self.pushButton_Op4.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_Op4.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Op4.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Op4.setObjectName("pushButton_Op4")
        self.pushButton_Op3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Op3.setGeometry(QtCore.QRect(398, 130, 75, 30))
        self.pushButton_Op3.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_Op3.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Op3.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Op3.setObjectName("pushButton_Op3")
        self.pushButton_Op5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Op5.setGeometry(QtCore.QRect(559, 130, 75, 30))
        self.pushButton_Op5.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_Op5.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Op5.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Op5.setObjectName("pushButton_Op5")
        self.pushButton_Op6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Op6.setGeometry(QtCore.QRect(638, 130, 75, 30))
        self.pushButton_Op6.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_Op6.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Op6.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Op6.setObjectName("pushButton_Op6")
        self.pushButton_Op7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Op7.setGeometry(QtCore.QRect(717, 130, 75, 30))
        self.pushButton_Op7.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_Op7.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Op7.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Op7.setObjectName("pushButton_Op7")
        self.pushButton_Op8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Op8.setGeometry(QtCore.QRect(796, 130, 75, 30))
        self.pushButton_Op8.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_Op8.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Op8.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Op8.setObjectName("pushButton_Op8")
        self.comboBox_OpcionesBuscar = QtWidgets.QComboBox(self.frame)
        self.comboBox_OpcionesBuscar.setGeometry(QtCore.QRect(353, 230, 181, 31))
        self.comboBox_OpcionesBuscar.setMinimumSize(QtCore.QSize(181, 31))
        self.comboBox_OpcionesBuscar.setMaximumSize(QtCore.QSize(181, 31))
        self.comboBox_OpcionesBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox_OpcionesBuscar.setObjectName("comboBox_OpcionesBuscar")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.pushButton_Buscar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Buscar.setGeometry(QtCore.QRect(796, 230, 75, 31))
        self.pushButton_Buscar.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_Buscar.setMaximumSize(QtCore.QSize(75, 31))
        self.pushButton_Buscar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Buscar.setObjectName("pushButton_Buscar")
        self.comboBox_OpcionesBuscar.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.comboBox.raise_()
        self.tableWidget.raise_()
        self.pushButton_Exit.raise_()
        self.textEdit_UserBuscar.raise_()
        self.label_4.raise_()
        self.pushButton_Registro.raise_()
        self.pushButton_Inactivar.raise_()
        self.pushButton_Modficiar.raise_()
        self.pushButton_Eliminar.raise_()
        self.label_5.raise_()
        self.pushButton_Op1.raise_()
        self.pushButton_Op2.raise_()
        self.pushButton_Op4.raise_()
        self.pushButton_Op3.raise_()
        self.pushButton_Op5.raise_()
        self.pushButton_Op6.raise_()
        self.pushButton_Op7.raise_()
        self.pushButton_Op8.raise_()
        self.pushButton_Buscar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
        self.label_3.setText(_translate("MainWindow", "Módulo de reportería"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Reportería"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1. Artistas por área"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2. Géneros con más canciones"))
        self.comboBox.setItemText(3, _translate("MainWindow", "3. Artistas con más albums individuales"))
        self.comboBox.setItemText(4, _translate("MainWindow", "4. Canciones de mayor duración con la información de sus artistas"))
        self.comboBox.setItemText(5, _translate("MainWindow", "5. Usuarios que han registrado más canciones"))
        self.comboBox.setItemText(6, _translate("MainWindow", "6. Promedio de duración de canciones por género"))
        self.comboBox.setItemText(7, _translate("MainWindow", "7. Álbumes más recientes"))
        self.comboBox.setItemText(8, _translate("MainWindow", "8. Artistas más colaborativos"))
        self.label_7.setText(_translate("MainWindow", "Módulo de autorización"))
        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "aqui"))
        # item = self.tableWidget.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "van"))
        # item = self.tableWidget.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "New Row"))
        # item = self.tableWidget.verticalHeaderItem(3)
        # item.setText(_translate("MainWindow", "las"))
        # item = self.tableWidget.verticalHeaderItem(4)
        # item.setText(_translate("MainWindow", "filas"))
        # item = self.tableWidget.verticalHeaderItem(5)
        # item.setText(_translate("MainWindow", "proyecto"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "aqui"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "van"))
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("MainWindow", "las"))
        # item = self.tableWidget.horizontalHeaderItem(3)
        # item.setText(_translate("MainWindow", "columnas"))
        # item = self.tableWidget.horizontalHeaderItem(4)
        # item.setText(_translate("MainWindow", "proyecto"))
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
        self.label_5.setText(_translate("MainWindow", "(Para recibir un reporte, vea la lista y luego presione el botón del reporte que desea obtener)"))
        self.pushButton_Op1.setText(_translate("MainWindow", "Opción 1"))
        self.pushButton_Op2.setText(_translate("MainWindow", "Opción 2"))
        self.pushButton_Op4.setText(_translate("MainWindow", "Opción 4"))
        self.pushButton_Op3.setText(_translate("MainWindow", "Opción 3"))
        self.pushButton_Op5.setText(_translate("MainWindow", "Opción 5"))
        self.pushButton_Op6.setText(_translate("MainWindow", "Opción 6"))
        self.pushButton_Op7.setText(_translate("MainWindow", "Opción 7"))
        self.pushButton_Op8.setText(_translate("MainWindow", "Opción 8"))
        self.comboBox_OpcionesBuscar.setItemText(0, _translate("MainWindow", "¿Qué deseas buscar?"))
        self.comboBox_OpcionesBuscar.setItemText(1, _translate("MainWindow", "Artista"))
        self.comboBox_OpcionesBuscar.setItemText(2, _translate("MainWindow", "Género"))
        self.comboBox_OpcionesBuscar.setItemText(3, _translate("MainWindow", "Álbum"))
        self.comboBox_OpcionesBuscar.setItemText(4, _translate("MainWindow", "Canción"))
        self.pushButton_Buscar.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_Buscar.clicked.connect(self.populateTable)


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

    def openVentanaOpciones(self):
        self.window = QtWidgets.QMainWindow()
        self.window.resize(1000,500)
        self.window.show()

    def populateTable(self):
        #clear the table
        self.tableWidget.setRowCount(0)
        if(self.textEdit_UserBuscar.toPlainText()!='' and self.comboBox_OpcionesBuscar.currentText() != '¿Qué deseas buscar?' ):
            print('Bien')
            conn = bd.connect(user= 'postgres', password = '59809690', host ="127.0.0.1",port = "5432", database = "NuevaPrueba")
            cursor = conn.cursor()
            if(self.comboBox_OpcionesBuscar.currentText() == 'Artista'):
                query = "SELECT name, composer FROM track WHERE composer ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                self.tableWidget.setColumnCount(len(record[0]))
                if(len(record)!= 0):
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))


            elif(self.comboBox_OpcionesBuscar.currentText() == 'Género'):
                query = "SELECT track.name, genre.name FROM track INNER JOIN genre ON track.genreid = genre.genreid WHERE genre.name ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                self.tableWidget.setColumnCount(len(record[0]))
                if(len(record)!= 0):
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))

            elif(self.comboBox_OpcionesBuscar.currentText() == 'Álbum'):
                query = "SELECT track.name FROM track INNER JOIN album ON track.albumid = album.albumid WHERE album.title ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                self.tableWidget.setColumnCount(len(record[0]))
                if(len(record)!= 0):
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))
                
            elif(self.comboBox_OpcionesBuscar.currentText() == 'Canción'):
                query = "SELECT * FROM track  WHERE name ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                self.tableWidget.setColumnCount(len(record[0]))
                if(len(record)!= 0):
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))
        else:    
            print('Mal')

