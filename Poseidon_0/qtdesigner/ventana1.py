# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(250, 175)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_Ventana1 = QtGui.QLabel(self.centralwidget)
        self.label_Ventana1.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_Ventana1.setObjectName(_fromUtf8("label_Ventana1"))
        self.pushButton_Ventana2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Ventana2.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.pushButton_Ventana2.setObjectName(_fromUtf8("pushButton_Ventana2"))
        self.lineEdit_Ventana1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Ventana1.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.lineEdit_Ventana1.setObjectName(_fromUtf8("lineEdit_Ventana1"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMen = QtGui.QMenu(self.menubar)
        self.menuMen.setObjectName(_fromUtf8("menuMen"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionVentana_2 = QtGui.QAction(MainWindow)
        self.actionVentana_2.setObjectName(_fromUtf8("actionVentana_2"))
        self.menuMen.addAction(self.actionVentana_2)
        self.menubar.addAction(self.menuMen.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_Ventana1.setText(_translate("MainWindow", "Ventana 1", None))
        self.pushButton_Ventana2.setText(_translate("MainWindow", "Ventana 2", None))
        self.menuMen.setTitle(_translate("MainWindow", "Menú", None))
        self.actionVentana_2.setText(_translate("MainWindow", "Ventana 2", None))

