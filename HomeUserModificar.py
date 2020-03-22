# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeUserModificar.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeUserModificar(object):
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
        self.pushButton_Exit = QtWidgets.QPushButton(self.frame)
        self.pushButton_Exit.setGeometry(QtCore.QRect(756, 50, 114, 32))
        self.pushButton_Exit.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_Exit.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_Exit.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 130, 210, 25))
        self.label_8.setMinimumSize(QtCore.QSize(210, 25))
        self.label_8.setMaximumSize(QtCore.QSize(210, 25))
        self.label_8.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_8.setObjectName("label_8")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(30, 150, 220, 30))
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
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 240, 100, 25))
        self.label_3.setMinimumSize(QtCore.QSize(100, 25))
        self.label_3.setMaximumSize(QtCore.QSize(100, 25))
        self.label_3.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_3.setObjectName("label_3")
        self.textEdit_Username = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Username.setGeometry(QtCore.QRect(30, 260, 220, 30))
        self.textEdit_Username.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_Username.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_Username.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_Username.setObjectName("textEdit_Username")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(506, 240, 100, 25))
        self.label_4.setMinimumSize(QtCore.QSize(100, 25))
        self.label_4.setMaximumSize(QtCore.QSize(100, 25))
        self.label_4.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_4.setObjectName("label_4")
        self.textEdit_Username_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Username_2.setGeometry(QtCore.QRect(506, 260, 220, 30))
        self.textEdit_Username_2.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_2.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_2.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_Username_2.setObjectName("textEdit_Username_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 220, 50))
        self.label_6.setMinimumSize(QtCore.QSize(220, 50))
        self.label_6.setMaximumSize(QtCore.QSize(220, 50))
        self.label_6.setStyleSheet("font: 21pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(506, 190, 220, 50))
        self.label_7.setMinimumSize(QtCore.QSize(220, 50))
        self.label_7.setMaximumSize(QtCore.QSize(220, 50))
        self.label_7.setStyleSheet("font: 21pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 330, 220, 50))
        self.label_9.setMinimumSize(QtCore.QSize(220, 50))
        self.label_9.setMaximumSize(QtCore.QSize(220, 50))
        self.label_9.setStyleSheet("font: 21pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 380, 100, 25))
        self.label_10.setMinimumSize(QtCore.QSize(100, 25))
        self.label_10.setMaximumSize(QtCore.QSize(100, 25))
        self.label_10.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_10.setObjectName("label_10")
        self.textEdit_Username_4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Username_4.setGeometry(QtCore.QRect(30, 400, 220, 30))
        self.textEdit_Username_4.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_4.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_4.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_Username_4.setObjectName("textEdit_Username_4")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(30, 450, 100, 25))
        self.label_11.setMinimumSize(QtCore.QSize(100, 25))
        self.label_11.setMaximumSize(QtCore.QSize(100, 25))
        self.label_11.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_11.setObjectName("label_11")
        self.textEdit_Username_5 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Username_5.setGeometry(QtCore.QRect(30, 470, 220, 30))
        self.textEdit_Username_5.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_5.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_5.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_Username_5.setObjectName("textEdit_Username_5")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(340, 380, 100, 25))
        self.label_12.setMinimumSize(QtCore.QSize(100, 25))
        self.label_12.setMaximumSize(QtCore.QSize(100, 25))
        self.label_12.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_12.setObjectName("label_12")
        self.textEdit_Username_6 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Username_6.setGeometry(QtCore.QRect(340, 400, 220, 30))
        self.textEdit_Username_6.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_6.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_6.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_Username_6.setObjectName("textEdit_Username_6")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(340, 450, 100, 25))
        self.label_13.setMinimumSize(QtCore.QSize(100, 25))
        self.label_13.setMaximumSize(QtCore.QSize(100, 25))
        self.label_13.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_13.setObjectName("label_13")
        self.textEdit_Username_7 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Username_7.setGeometry(QtCore.QRect(340, 470, 220, 30))
        self.textEdit_Username_7.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_7.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_7.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_Username_7.setObjectName("textEdit_Username_7")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(650, 380, 100, 25))
        self.label_14.setMinimumSize(QtCore.QSize(100, 25))
        self.label_14.setMaximumSize(QtCore.QSize(100, 25))
        self.label_14.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_14.setObjectName("label_14")
        self.textEdit_Username_8 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Username_8.setGeometry(QtCore.QRect(650, 400, 220, 30))
        self.textEdit_Username_8.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_8.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_Username_8.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_Username_8.setObjectName("textEdit_Username_8")
        self.pushButton_MAlbum = QtWidgets.QPushButton(self.frame)
        self.pushButton_MAlbum.setGeometry(QtCore.QRect(756, 260, 114, 32))
        self.pushButton_MAlbum.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_MAlbum.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_MAlbum.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_MAlbum.setObjectName("pushButton_MAlbum")
        self.pushButton_MArtista = QtWidgets.QPushButton(self.frame)
        self.pushButton_MArtista.setGeometry(QtCore.QRect(280, 260, 114, 32))
        self.pushButton_MArtista.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_MArtista.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_MArtista.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_MArtista.setObjectName("pushButton_MArtista")
        self.pushButton_MCancion = QtWidgets.QPushButton(self.frame)
        self.pushButton_MCancion.setGeometry(QtCore.QRect(705, 470, 114, 32))
        self.pushButton_MCancion.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_MCancion.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_MCancion.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_MCancion.setObjectName("pushButton_MCancion")
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_Exit.raise_()
        self.comboBox_3.raise_()
        self.label_3.raise_()
        self.textEdit_Username.raise_()
        self.label_4.raise_()
        self.textEdit_Username_2.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.textEdit_Username_4.raise_()
        self.label_11.raise_()
        self.textEdit_Username_5.raise_()
        self.label_12.raise_()
        self.textEdit_Username_6.raise_()
        self.label_13.raise_()
        self.textEdit_Username_7.raise_()
        self.label_14.raise_()
        self.textEdit_Username_8.raise_()
        self.pushButton_MAlbum.raise_()
        self.pushButton_MArtista.raise_()
        self.pushButton_MCancion.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
        self.pushButton_Exit.setText(_translate("MainWindow", "Exit"))
        self.label_8.setText(_translate("MainWindow", "Módulo de Autorización"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Autorización"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Registros"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Inactivación"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Modificación"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Inactivación"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.textEdit_Username.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Nombre"))
        self.textEdit_Username_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Registro Artistas"))
        self.label_7.setText(_translate("MainWindow", "Registro Álbumes"))
        self.label_9.setText(_translate("MainWindow", "Registro Canciones"))
        self.label_10.setText(_translate("MainWindow", "Nombre"))
        self.textEdit_Username_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Miliseconds"))
        self.textEdit_Username_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "UnitPrice"))
        self.textEdit_Username_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Composer"))
        self.textEdit_Username_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Bytes"))
        self.textEdit_Username_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.pushButton_MAlbum.setText(_translate("MainWindow", "Modificar"))
        self.pushButton_MArtista.setText(_translate("MainWindow", "Modificar"))
        self.pushButton_MCancion.setText(_translate("MainWindow", "Modificar"))
