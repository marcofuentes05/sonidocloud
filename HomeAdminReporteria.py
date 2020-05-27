# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeAdminReporteria.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
import sys
import psycopg2 as bd
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeAdminReporteria(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 650))
        MainWindow.setStyleSheet("background-color: rgb(72,35,60);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 50, 900, 550))
        self.frame.setMinimumSize(QtCore.QSize(900, 550))
        self.frame.setMaximumSize(QtCore.QSize(900, 550))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 30, 205, 50))
        self.label.setMinimumSize(QtCore.QSize(205, 50))
        self.label.setMaximumSize(QtCore.QSize(205, 50))
        self.label.setStyleSheet("font: 24pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(30, 270, 480, 161))
        self.tableWidget.setMinimumSize(QtCore.QSize(480, 161))
        self.tableWidget.setMaximumSize(QtCore.QSize(480, 161))
        self.tableWidget.setStyleSheet("font: 13pt \"Times\";\n"
"color: rgb(64, 55, 110);\n"
"background-color: rgb(212, 228, 188);")
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(4)
        # self.tableWidget.setRowCount(5)
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
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(3, item)
        self.textEdit_IngresarArtista = QtWidgets.QTextEdit(self.frame)
        self.textEdit_IngresarArtista.setGeometry(QtCore.QRect(30, 210, 200, 31))
        self.textEdit_IngresarArtista.setMinimumSize(QtCore.QSize(200, 31))
        self.textEdit_IngresarArtista.setMaximumSize(QtCore.QSize(200, 31))
        self.textEdit_IngresarArtista.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit_IngresarArtista.setObjectName("textEdit_IngresarArtista")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 100, 210, 25))
        self.label_8.setMinimumSize(QtCore.QSize(210, 25))
        self.label_8.setMaximumSize(QtCore.QSize(210, 25))
        self.label_8.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_8.setObjectName("label_8")
        self.comboBox_OpcionesBuscarFecha = QtWidgets.QComboBox(self.frame)
        self.comboBox_OpcionesBuscarFecha.setGeometry(QtCore.QRect(30, 130, 400, 31))
        self.comboBox_OpcionesBuscarFecha.setMinimumSize(QtCore.QSize(400, 31))
        self.comboBox_OpcionesBuscarFecha.setMaximumSize(QtCore.QSize(400, 31))
        self.comboBox_OpcionesBuscarFecha.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox_OpcionesBuscarFecha.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_OpcionesBuscarFecha.setObjectName("comboBox_OpcionesBuscarFecha")
        self.comboBox_OpcionesBuscarFecha.addItem("")
        self.comboBox_OpcionesBuscarFecha.addItem("")
        self.comboBox_OpcionesBuscarFecha.addItem("")
        self.comboBox_OpcionesBuscarFecha.addItem("")
        self.comboBox_OpcionesBuscarFecha.addItem("")
        self.pushButton_Reportar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Reportar.setGeometry(QtCore.QRect(430, 490, 80, 31))
        self.pushButton_Reportar.setMinimumSize(QtCore.QSize(80, 31))
        self.pushButton_Reportar.setMaximumSize(QtCore.QSize(80, 31))
        self.pushButton_Reportar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Reportar.setObjectName("pushButton_Reportar")
        self.calendarWidget_Final = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget_Final.setGeometry(QtCore.QRect(570, 360, 310, 171))
        self.calendarWidget_Final.setMinimumSize(QtCore.QSize(310, 171))
        self.calendarWidget_Final.setMaximumSize(QtCore.QSize(310, 171))
        self.calendarWidget_Final.setObjectName("calendarWidget_Final")
        self.calendarWidget_Inicial = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget_Inicial.setGeometry(QtCore.QRect(570, 130, 310, 171))
        self.calendarWidget_Inicial.setMinimumSize(QtCore.QSize(310, 171))
        self.calendarWidget_Inicial.setMaximumSize(QtCore.QSize(310, 171))
        self.calendarWidget_Inicial.setObjectName("calendarWidget_Inicial")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 180, 200, 25))
        self.label_9.setMinimumSize(QtCore.QSize(200, 25))
        self.label_9.setMaximumSize(QtCore.QSize(200, 25))
        self.label_9.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_9.setObjectName("label_9")
        self.comboBox_OpcionesBuscar = QtWidgets.QComboBox(self.frame)
        self.comboBox_OpcionesBuscar.setGeometry(QtCore.QRect(30, 490, 400, 31))
        self.comboBox_OpcionesBuscar.setMinimumSize(QtCore.QSize(400, 31))
        self.comboBox_OpcionesBuscar.setMaximumSize(QtCore.QSize(360, 31))
        self.comboBox_OpcionesBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox_OpcionesBuscar.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_OpcionesBuscar.setMinimumContentsLength(0)
        self.comboBox_OpcionesBuscar.setObjectName("comboBox_OpcionesBuscar")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.comboBox_OpcionesBuscar.addItem("")
        self.pushButton_ReportarPorFecha = QtWidgets.QPushButton(self.frame)
        self.pushButton_ReportarPorFecha.setGeometry(QtCore.QRect(430, 210, 80, 31))
        self.pushButton_ReportarPorFecha.setMinimumSize(QtCore.QSize(80, 31))
        self.pushButton_ReportarPorFecha.setMaximumSize(QtCore.QSize(80, 31))
        self.pushButton_ReportarPorFecha.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_ReportarPorFecha.setObjectName("pushButton_ReportarPorFecha")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 460, 210, 25))
        self.label_10.setMinimumSize(QtCore.QSize(210, 25))
        self.label_10.setMaximumSize(QtCore.QSize(210, 25))
        self.label_10.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(570, 100, 210, 25))
        self.label_11.setMinimumSize(QtCore.QSize(210, 25))
        self.label_11.setMaximumSize(QtCore.QSize(210, 25))
        self.label_11.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(570, 330, 210, 25))
        self.label_12.setMinimumSize(QtCore.QSize(210, 25))
        self.label_12.setMaximumSize(QtCore.QSize(210, 25))
        self.label_12.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_9.raise_()
        self.label_12.raise_()
        self.label_11.raise_()
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tableWidget.raise_()
        self.textEdit_IngresarArtista.raise_()
        self.comboBox_OpcionesBuscarFecha.raise_()
        self.pushButton_Reportar.raise_()
        self.calendarWidget_Final.raise_()
        self.calendarWidget_Inicial.raise_()
        self.pushButton_ReportarPorFecha.raise_()
        self.label_10.raise_()
        self.comboBox_OpcionesBuscar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
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
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "aqui"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "van"))
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("MainWindow", "las"))
        # item = self.tableWidget.horizontalHeaderItem(3)
        # item.setText(_translate("MainWindow", "columnas"))
        self.textEdit_IngresarArtista.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Reportería por fechas"))
        self.comboBox_OpcionesBuscarFecha.setItemText(0, _translate("MainWindow", "Reportería por fecha"))
        self.comboBox_OpcionesBuscarFecha.setItemText(1, _translate("MainWindow", "1. Total de ventas por semana"))
        self.comboBox_OpcionesBuscarFecha.setItemText(2, _translate("MainWindow", "2. Los N artistas con las mayores ventas por fechas"))
        self.comboBox_OpcionesBuscarFecha.setItemText(3, _translate("MainWindow", "3. Total de ventas por género"))
        self.comboBox_OpcionesBuscarFecha.setItemText(4, _translate("MainWindow", "4. Las N canciones con más reproducciones para un artista"))
        self.pushButton_Reportar.setText(_translate("MainWindow", "Reportar"))
        self.pushButton_Reportar.clicked.connect(self.report)
        self.label_9.setText(_translate("MainWindow", "Ingrese artista"))
        self.comboBox_OpcionesBuscar.setItemText(0, _translate("MainWindow", "Reportería"))
        self.comboBox_OpcionesBuscar.setItemText(1, _translate("MainWindow", "1. Los 5 artistas con más álbumes publicados"))
        self.comboBox_OpcionesBuscar.setItemText(2, _translate("MainWindow", "2. Los 5 géneros con más canciones"))
        self.comboBox_OpcionesBuscar.setItemText(3, _translate("MainWindow", "3. Total de duración de cada playlist"))
        self.comboBox_OpcionesBuscar.setItemText(4, _translate("MainWindow", "4. Las 5 canciones de mayor duración con información del artista"))
        self.comboBox_OpcionesBuscar.setItemText(5, _translate("MainWindow", "5. Los 5 usuarios que han registrado más canciones"))
        self.comboBox_OpcionesBuscar.setItemText(6, _translate("MainWindow", "6. Promedio de duración de canciones por género"))
        self.comboBox_OpcionesBuscar.setItemText(7, _translate("MainWindow", "7. Cantidad de artistas diferentes por playlist"))
        self.comboBox_OpcionesBuscar.setItemText(8, _translate("MainWindow", "8. Los 5 artistas con más diversidad de géneros"))
        self.pushButton_ReportarPorFecha.setText(_translate("MainWindow", "Reportar"))
        self.label_10.setText(_translate("MainWindow", "Reportería"))
        self.label_11.setText(_translate("MainWindow", "Escoja fecha inicial"))
        self.label_12.setText(_translate("MainWindow", "Escoja fecha final"))


    def openPopUpError(self, mensaje):
        msgError = QMessageBox()
        msgError.setText(mensaje)
        msgError.setIcon(QMessageBox.Warning)
        x = msgError.exec_()

    def openPopUpCheck(self, mensaje):
        msgGood = QMessageBox()
        msgGood.setText(mensaje)
        msgGood.setIcon(QMessageBox.Information)
        y = msgGood.exec_()

    def populateTable(self):
        #clear the table
        self.tableWidget.setRowCount(0)
        if(self.textEdit_UserBuscar.toPlainText()!='' and self.comboBox_OpcionesBuscar.currentText() != '¿Qué deseas buscar?' ):
            print('Bien')
            conn = None
            params =config()
            conn = bd.connect(**params)
            cursor = conn.cursor()
            if(self.comboBox_OpcionesBuscar.currentText() == 'Artista'):
                query = "SELECT track.name, artist.name FROM track JOIN album ON track.albumid = album.albumid JOIN artist ON album.artistid = artist.artistid WHERE artist.name ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                print(record)
                if(len(record)!= 0):
                    self.tableWidget.setColumnCount(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            print(i,j)
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))


            elif(self.comboBox_OpcionesBuscar.currentText() == 'Género'):
                query = "SELECT track.name, genre.name FROM track INNER JOIN genre ON track.genreid = genre.genreid WHERE genre.name ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                if(len(record)!= 0):
                    self.tableWidget.setColumnCount(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))

            elif(self.comboBox_OpcionesBuscar.currentText() == 'Álbum'):
                query = "SELECT track.name FROM track INNER JOIN album ON track.albumid = album.albumid WHERE album.title ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                if(len(record)!= 0):
                    self.tableWidget.setColumnCount(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))

            elif(self.comboBox_OpcionesBuscar.currentText() == 'Canción'):
                query = "SELECT * FROM track  WHERE name ~* \'" + self.textEdit_UserBuscar.toPlainText() +"'"
                cursor.execute(query)
                record = cursor.fetchall()
                if(len(record)!= 0):
                    self.tableWidget.setColumnCount(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))
        else:
            print('Mal')

    def populateTableOpcion1(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query1()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))

    def populateTableOpcion2(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query2()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))

    def populateTableOpcion3(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query3()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))

    def populateTableOpcion4(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query4()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))

    def populateTableOpcion5(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query5()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))

    def populateTableOpcion6(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query6()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))

    def populateTableOpcion7(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query7()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))

    def populateTableOpcion8(self):
        self.tableWidget.setRowCount(0)
        conn = None
        params =config()
        conn = bd.connect(**params)
        cursor = conn.cursor()
        query = query8()
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(record[i][j])))


    def report(self):
        if(self.comboBox_OpcionesBuscar.currentText()=="Reportería"):
            print("Eliga una opcion")
        elif(self.comboBox_OpcionesBuscar.currentText()=="1. Los 5 artistas con más álbumes publicados"):
            self.populateTableOpcion1()
        elif(self.comboBox_OpcionesBuscar.currentText()=="2. Los 5 géneros con más canciones"):
            self.populateTableOpcion2()
        elif(self.comboBox_OpcionesBuscar.currentText()=="3. Total de duración de cada playlist"):
            self.populateTableOpcion3()
        elif(self.comboBox_OpcionesBuscar.currentText()=="4. Las 5 canciones de mayor duración con información del artista"):
            self.populateTableOpcion4()
        elif(self.comboBox_OpcionesBuscar.currentText()=="5. Los 5 usuarios que han registrado más canciones"):
            self.populateTableOpcion5()
        elif(self.comboBox_OpcionesBuscar.currentText()=="6. Promedio de duración de canciones por género"):
            self.populateTableOpcion6()
        elif(self.comboBox_OpcionesBuscar.currentText()=="7. Cantidad de artistas diferentes por playlist"):
            self.populateTableOpcion7()
        elif(self.comboBox_OpcionesBuscar.currentText()=="8. Los 5 artistas con más diversidad de géneros"):
            self.populateTableOpcion8()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    HomeAdmin = QtWidgets.QMainWindow()
    ui = Ui_HomeAdmin()
    ui.setupUi(HomeAdmin)
    HomeAdmin.show()
    sys.exit(app.exec_())

