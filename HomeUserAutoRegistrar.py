# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeUserAutoRegistrar.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeUserAutoRegistrar(object):
    def __init__(self, id):
        super(Ui_HomeUserAuto, self).__init__()
        self.id = id
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
"border-radius: 12px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 60, 235, 100))
        self.label.setMinimumSize(QtCore.QSize(235, 100))
        self.label.setMaximumSize(QtCore.QSize(205, 50))
        self.label.setStyleSheet("font: 32pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 180, 180))
        self.label_2.setMinimumSize(QtCore.QSize(180, 180))
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
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 240, 100, 25))
        self.label_3.setMinimumSize(QtCore.QSize(100, 25))
        self.label_3.setMaximumSize(QtCore.QSize(100, 25))
        self.label_3.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_3.setObjectName("label_3")
        self.textEdit_RArtistaNombre = QtWidgets.QTextEdit(self.frame)
        self.textEdit_RArtistaNombre.setGeometry(QtCore.QRect(30, 260, 220, 30))
        self.textEdit_RArtistaNombre.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_RArtistaNombre.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_RArtistaNombre.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_RArtistaNombre.setObjectName("textEdit_RArtistaNombre")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(340, 240, 150, 25))
        self.label_4.setMinimumSize(QtCore.QSize(150, 25))
        self.label_4.setMaximumSize(QtCore.QSize(150, 25))
        self.label_4.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_4.setObjectName("label_4")
        self.textEdit_RAlbumNombre = QtWidgets.QTextEdit(self.frame)
        self.textEdit_RAlbumNombre.setGeometry(QtCore.QRect(340, 260, 220, 30))
        self.textEdit_RAlbumNombre.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_RAlbumNombre.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_RAlbumNombre.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_RAlbumNombre.setObjectName("textEdit_RAlbumNombre")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 220, 50))
        self.label_6.setMinimumSize(QtCore.QSize(220, 50))
        self.label_6.setMaximumSize(QtCore.QSize(220, 50))
        self.label_6.setStyleSheet("font: 21pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 340, 220, 50))
        self.label_9.setMinimumSize(QtCore.QSize(220, 50))
        self.label_9.setMaximumSize(QtCore.QSize(220, 50))
        self.label_9.setStyleSheet("font: 21pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 390, 100, 25))
        self.label_10.setMinimumSize(QtCore.QSize(100, 25))
        self.label_10.setMaximumSize(QtCore.QSize(100, 25))
        self.label_10.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_10.setObjectName("label_10")
        self.textEdit_RCancionesNombre = QtWidgets.QTextEdit(self.frame)
        self.textEdit_RCancionesNombre.setGeometry(QtCore.QRect(30, 410, 220, 30))
        self.textEdit_RCancionesNombre.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_RCancionesNombre.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_RCancionesNombre.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_RCancionesNombre.setObjectName("textEdit_RCancionesNombre")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(30, 460, 150, 25))
        self.label_11.setMinimumSize(QtCore.QSize(150, 25))
        self.label_11.setMaximumSize(QtCore.QSize(150, 25))
        self.label_11.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_11.setObjectName("label_11")
        self.textEdit_RCancionesMiliseconds = QtWidgets.QTextEdit(self.frame)
        self.textEdit_RCancionesMiliseconds.setGeometry(QtCore.QRect(30, 480, 220, 30))
        self.textEdit_RCancionesMiliseconds.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_RCancionesMiliseconds.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_RCancionesMiliseconds.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_RCancionesMiliseconds.setObjectName("textEdit_RCancionesMiliseconds")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(340, 390, 100, 25))
        self.label_12.setMinimumSize(QtCore.QSize(100, 25))
        self.label_12.setMaximumSize(QtCore.QSize(100, 25))
        self.label_12.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_12.setObjectName("label_12")
        self.textEdit_RCancionesUnitPrice = QtWidgets.QTextEdit(self.frame)
        self.textEdit_RCancionesUnitPrice.setGeometry(QtCore.QRect(340, 410, 220, 30))
        self.textEdit_RCancionesUnitPrice.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_RCancionesUnitPrice.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_RCancionesUnitPrice.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_RCancionesUnitPrice.setObjectName("textEdit_RCancionesUnitPrice")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(340, 460, 100, 25))
        self.label_13.setMinimumSize(QtCore.QSize(100, 25))
        self.label_13.setMaximumSize(QtCore.QSize(100, 25))
        self.label_13.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_13.setObjectName("label_13")
        self.textEdit_RCancionesAlbum = QtWidgets.QTextEdit(self.frame)
        self.textEdit_RCancionesAlbum.setGeometry(QtCore.QRect(340, 480, 220, 30))
        self.textEdit_RCancionesAlbum.setMinimumSize(QtCore.QSize(220, 30))
        self.textEdit_RCancionesAlbum.setMaximumSize(QtCore.QSize(220, 30))
        self.textEdit_RCancionesAlbum.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
        self.textEdit_RCancionesAlbum.setObjectName("textEdit_RCancionesAlbum")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(650, 390, 100, 25))
        self.label_14.setMinimumSize(QtCore.QSize(100, 25))
        self.label_14.setMaximumSize(QtCore.QSize(100, 25))
        self.label_14.setStyleSheet("font: 18pt \"Times\";\n"
"color: rgb(10, 54, 157);\n"
"")
        self.label_14.setObjectName("label_14")
        self.pushButton_RAlbum = QtWidgets.QPushButton(self.frame)
        self.pushButton_RAlbum.setGeometry(QtCore.QRect(650, 260, 114, 32))
        self.pushButton_RAlbum.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_RAlbum.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_RAlbum.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_RAlbum.setObjectName("pushButton_RAlbum")
        self.pushButton_RCancion = QtWidgets.QPushButton(self.frame)
        self.pushButton_RCancion.setGeometry(QtCore.QRect(705, 480, 114, 32))
        self.pushButton_RCancion.setMinimumSize(QtCore.QSize(114, 32))
        self.pushButton_RCancion.setMaximumSize(QtCore.QSize(114, 32))
        self.pushButton_RCancion.setStyleSheet("background-color: rgb(10, 54, 157);\n"
"font: 14pt \"Times\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_RCancion.setObjectName("pushButton_RCancion")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(650, 410, 220, 30))
        self.comboBox.setMinimumSize(QtCore.QSize(220, 30))
        self.comboBox.setStyleSheet("background-color: rgb(150, 172, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Times\";")
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_Exit.raise_()
        self.label_3.raise_()
        self.textEdit_RArtistaNombre.raise_()
        self.textEdit_RAlbumNombre.raise_()
        self.label_6.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.textEdit_RCancionesNombre.raise_()
        self.label_11.raise_()
        self.textEdit_RCancionesMiliseconds.raise_()
        self.label_12.raise_()
        self.textEdit_RCancionesUnitPrice.raise_()
        self.label_13.raise_()
        self.textEdit_RCancionesAlbum.raise_()
        self.label_14.raise_()
        self.pushButton_RAlbum.raise_()
        self.pushButton_RCancion.raise_()
        self.comboBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sonido Cloud "))
        self.pushButton_Exit.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.textEdit_RArtistaNombre.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Nombre Artista"))
        self.textEdit_RAlbumNombre.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Registro Álbumes"))
        self.label_9.setText(_translate("MainWindow", "Registro Canciones"))
        self.label_10.setText(_translate("MainWindow", "Nombre"))
        self.textEdit_RCancionesNombre.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Milisegundos"))
        self.textEdit_RCancionesMiliseconds.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "UnitPrice"))
        self.textEdit_RCancionesUnitPrice.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Álbum"))
        self.textEdit_RCancionesAlbum.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\';\"><br /></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Género"))
        self.pushButton_RAlbum.setText(_translate("MainWindow", "Registrar"))
        self.pushButton_RCancion.setText(_translate("MainWindow", "Registrar"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Escoga un género"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Rock"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Jazz"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Metal"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Alternative & Punk"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Rock And Roll"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Blues"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Latin"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Reggae"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Pop"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Soundtrack"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Bossa Nova"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Easy Listening"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Heavy Metal"))
        self.comboBox.setItemText(14, _translate("MainWindow", "R&B/Soul"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Electronica/Dance"))
        self.comboBox.setItemText(16, _translate("MainWindow", "World"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Hip Hop/Rap"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Science Fiction"))
        self.comboBox.setItemText(19, _translate("MainWindow", "TV Shows"))
        self.comboBox.setItemText(20, _translate("MainWindow", "Sci Fi & Fantasy"))
        self.comboBox.setItemText(21, _translate("MainWindow", "Drama"))
        self.comboBox.setItemText(22, _translate("MainWindow", "Comedy"))
        self.comboBox.setItemText(23, _translate("MainWindow", "Alternative"))
        self.comboBox.setItemText(24, _translate("MainWindow", "Classical"))
        self.comboBox.setItemText(25, _translate("MainWindow", "Opera"))
