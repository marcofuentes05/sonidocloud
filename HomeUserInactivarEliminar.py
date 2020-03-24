# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeUserInactivarEliminar.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import psycopg2 as bd

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
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(609, 130, 230, 50))
        self.label_7.setMinimumSize(QtCore.QSize(220, 50))
        self.label_7.setMaximumSize(QtCore.QSize(230, 25))
        self.label_7.setStyleSheet("font: 19pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(534, 230, 337, 231))
        self.tableWidget.setMinimumSize(QtCore.QSize(337, 231))
        self.tableWidget.setMaximumSize(QtCore.QSize(337, 231))
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
        self.textEdit_UserBuscar.setGeometry(QtCore.QRect(565, 200, 231, 31))
        self.textEdit_UserBuscar.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"font: 13pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit_UserBuscar.setObjectName("textEdit_UserBuscar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(534, 199, 31, 31))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("finder.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(88, 130, 220, 50))
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
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 230, 337, 231))
        self.tableWidget_2.setMinimumSize(QtCore.QSize(337, 231))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(337, 231))
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
        self.pushButton_Login_2.setGeometry(QtCore.QRect(141, 480, 114, 32))
        self.pushButton_Login_2.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_Login_2.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_Login_2.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Login_2.setObjectName("pushButton_Login_2")
        self.pushButton_Login_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Login_3.setGeometry(QtCore.QRect(646, 490, 114, 32))
        self.pushButton_Login_3.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_Login_3.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_Login_3.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Login_3.setObjectName("pushButton_Login_3")
        self.pushButton_BuscarEliminar = QtWidgets.QPushButton(self.frame)
        self.pushButton_BuscarEliminar.setGeometry(QtCore.QRect(292, 200, 75, 31))
        self.pushButton_BuscarEliminar.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_BuscarEliminar.setMaximumSize(QtCore.QSize(75, 31))
        self.pushButton_BuscarEliminar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_BuscarEliminar.setObjectName("pushButton_BuscarEliminar")
        self.pushButton_BuscarInactivar = QtWidgets.QPushButton(self.frame)
        self.pushButton_BuscarInactivar.setGeometry(QtCore.QRect(796, 200, 75, 31))
        self.pushButton_BuscarInactivar.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_BuscarInactivar.setMaximumSize(QtCore.QSize(75, 31))
        self.pushButton_BuscarInactivar.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_BuscarInactivar.setObjectName("pushButton_BuscarInactivar")
        self.pushButton_BuscarInactivar.clicked.connect(self.inactivate)
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
        self.pushButton_BuscarEliminar.raise_()
        self.pushButton_BuscarInactivar.raise_()
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
        self.pushButton_BuscarEliminar.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_BuscarInactivar.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_BuscarInactivar.clicked.connect(self.populateTable)
        self.pushButton_Login_3.clicked.connect(self.inactivate)
        self.pushButton_BuscarEliminar.clicked.connect(self.search_delete)
        self.pushButton_Login_2.clicked.connect(self.deleteItem)
        self.pushButton_Login.clicked.connect(self.onExit)
    def populateTable(self):
        #clear the table
        self.tableWidget.setRowCount(0)
        if(self.textEdit_UserBuscar.toPlainText() != '' ):
            try:
                print('Bien')
                conn = bd.connect(user='marco', password='12345678',
                                  host="127.0.0.1", port="5432", database="proyectoNew")
                cursor = conn.cursor()
                texto = self.textEdit_UserBuscar.toPlainText()
                query = "SELECT track.name, album.title, artist.name FROM track JOIN album ON album.albumid = track.albumid JOIN artist ON album.artistid = artist.artistid WHERE track.name LIKE \'%"+texto+"%\' AND track.isactive = \'t\'"
                cursor.execute(query)
                record = cursor.fetchall()
                if(len(record) != 0 and len(record[0]) != 0):
                    self.tableWidget.setColumnCount(len(record[0]))
                    self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Cancion"))
                    self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Album"))
                    self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Artista"))
                    print(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget.insertRow(i)
                        for j in range(len(record[0])):
                            print(i, j)
                            self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(record[i][j]))
            except(Exception) as error:
                print("Error", error)
            finally:
                if(conn):
                   cursor.close()
                   conn.close()
                
        else:
            print('Mal')


    def search_delete(self):
        #clear the table
        self.tableWidget_2.setRowCount(0)
        if(self.textEdit_UserBuscar_2.toPlainText() != ''):
            print('Bien')
            try:
                conn = bd.connect(user='marco', password='12345678',
                                  host="127.0.0.1", port="5432", database="proyectoNew")
                cursor = conn.cursor()
                texto = self.textEdit_UserBuscar_2.toPlainText()
                query = "SELECT track.name, album.title, artist.name FROM track JOIN album ON album.albumid = track.albumid JOIN artist ON album.artistid = artist.artistid WHERE track.name LIKE \'%"+texto+"%\' AND track.isactive = \'t\'"
                cursor.execute(query)
                record = cursor.fetchall()
                if(len(record) != 0 and len(record[0]) != 0):
                    self.tableWidget_2.setColumnCount(len(record[0]))
                    self.tableWidget_2.setHorizontalHeaderItem(
                        0, QtWidgets.QTableWidgetItem("Cancion"))
                    self.tableWidget_2.setHorizontalHeaderItem(
                        1, QtWidgets.QTableWidgetItem("Album"))
                    self.tableWidget_2.setHorizontalHeaderItem(
                        2, QtWidgets.QTableWidgetItem("Artista"))
                    print(len(record[0]))
                    for i in range(len(record)):
                        self.tableWidget_2.insertRow(i)
                        for j in range(len(record[0])):
                            print(i, j)
                            self.tableWidget_2.setItem(
                                i, j, QtWidgets.QTableWidgetItem(record[i][j]))
            except (Exception) as error:
                    print("Error: ", error)
            finally:
                if(conn):
                   cursor.close()
                   conn.close()
        else:
            print('Mal')


    def inactivate(self):
            
            query1 = "UPDATE track SET isactive = FALSE WHERE name = \'" + str(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())+"\'"
            try:
                conn = bd.connect(user='marco', password='12345678',
                                  host="127.0.0.1", port="5432", database="proyectoNew")
                cursor = conn.cursor()
                cursor.execute(query1)
                conn.commit()
            except(Exception) as error:
                print("Error", error)
            finally:
                if(conn):
                   cursor.close()
                   conn.close()
            self.populateTable()


    def deleteItem(self):
        print(str(self.tableWidget_2.item(self.tableWidget_2.currentRow(),0).text()))
        nombre = self.tableWidget_2.item(self.tableWidget_2.currentRow(), 0).text()
        album = self.tableWidget_2.item(self.tableWidget_2.currentRow(),1).text()
        artista = self.tableWidget_2.item(self.tableWidget_2.currentRow(), 2).text()
        self.tableWidget_2.item(self.tableWidget_2.currentRow(), 0).text()
        query2 = "DELETE FROM track WHERE track.name = \'"+ nombre +"\'"
        try:
            conn = bd.connect(user='marco', password='12345678',
                              host="127.0.0.1", port="5432", database="proyectoNew")
            cursor = conn.cursor()
            cursor.execute(query2)
            print(cursor.statusmessage)
            if (cursor.statusmessage == 'DELETE 1'):
                conn.commit() 
        except(Exception) as error:
            print("EROOOR", error)
        finally:
            if(conn):
                cursor.close()
                conn.close()
        self.search_delete()


    def onExit(self):
            HomeUserActivarEliminar.hide()
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    HomeUserActivarEliminar = QtWidgets.QMainWindow()
    ui = Ui_HomeUserInactivarEliminar()
    ui.setupUi(HomeUserActivarEliminar)
    HomeUserActivarEliminar.show()
    sys.exit(app.exec_())
