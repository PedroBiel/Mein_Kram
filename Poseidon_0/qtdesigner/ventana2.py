# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana2.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(250, 150)
        self.label_Ventana2 = QtGui.QLabel(Form)
        self.label_Ventana2.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_Ventana2.setObjectName(_fromUtf8("label_Ventana2"))
        self.lineEdit_Ventana2 = QtGui.QLineEdit(Form)
        self.lineEdit_Ventana2.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.lineEdit_Ventana2.setObjectName(_fromUtf8("lineEdit_Ventana2"))
        self.pushButton_Ventana1 = QtGui.QPushButton(Form)
        self.pushButton_Ventana1.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.pushButton_Ventana1.setObjectName(_fromUtf8("pushButton_Ventana1"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_Ventana2.setText(_translate("Form", "Ventana 2", None))
        self.pushButton_Ventana1.setText(_translate("Form", "Ventana 1", None))

