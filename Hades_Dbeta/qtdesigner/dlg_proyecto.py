# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_proyecto.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(325, 251)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_datos_proyecto = QtGui.QLabel(Dialog)
        self.label_datos_proyecto.setObjectName(_fromUtf8("label_datos_proyecto"))
        self.gridLayout.addWidget(self.label_datos_proyecto, 0, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_proyecto = QtGui.QLabel(Dialog)
        self.label_proyecto.setObjectName(_fromUtf8("label_proyecto"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_proyecto)
        self.lineEdit_proyecto = QtGui.QLineEdit(Dialog)
        self.lineEdit_proyecto.setObjectName(_fromUtf8("lineEdit_proyecto"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_proyecto)
        self.label_elemento = QtGui.QLabel(Dialog)
        self.label_elemento.setObjectName(_fromUtf8("label_elemento"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_elemento)
        self.lineEdit_elemento = QtGui.QLineEdit(Dialog)
        self.lineEdit_elemento.setObjectName(_fromUtf8("lineEdit_elemento"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_elemento)
        self.label_empresa = QtGui.QLabel(Dialog)
        self.label_empresa.setObjectName(_fromUtf8("label_empresa"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_empresa)
        self.lineEdit_empresa = QtGui.QLineEdit(Dialog)
        self.lineEdit_empresa.setObjectName(_fromUtf8("lineEdit_empresa"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_empresa)
        self.label_autor = QtGui.QLabel(Dialog)
        self.label_autor.setObjectName(_fromUtf8("label_autor"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_autor)
        self.lineEdit_autor = QtGui.QLineEdit(Dialog)
        self.lineEdit_autor.setObjectName(_fromUtf8("lineEdit_autor"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_autor)
        self.label_comentarios = QtGui.QLabel(Dialog)
        self.label_comentarios.setObjectName(_fromUtf8("label_comentarios"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_comentarios)
        self.plainTextEdit_comentarios = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit_comentarios.setObjectName(_fromUtf8("plainTextEdit_comentarios"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.plainTextEdit_comentarios)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_aceptar = QtGui.QPushButton(Dialog)
        self.pushButton_aceptar.setObjectName(_fromUtf8("pushButton_aceptar"))
        self.horizontalLayout.addWidget(self.pushButton_aceptar)
        self.pushButton_cancelar = QtGui.QPushButton(Dialog)
        self.pushButton_cancelar.setObjectName(_fromUtf8("pushButton_cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_cancelar)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_datos_proyecto.setText(_translate("Dialog", "Datos de proyecto", None))
        self.label_proyecto.setText(_translate("Dialog", "Proyecto:", None))
        self.lineEdit_proyecto.setText(_translate("Dialog", "12345", None))
        self.label_elemento.setText(_translate("Dialog", "Elemento:", None))
        self.lineEdit_elemento.setText(_translate("Dialog", "GANGSEONGDAEGUK", None))
        self.label_empresa.setText(_translate("Dialog", "Empresa:", None))
        self.lineEdit_empresa.setText(_translate("Dialog", "JOSEON MINJUJUEUI INMIN GONGHWAGUK", None))
        self.label_autor.setText(_translate("Dialog", "Autor:", None))
        self.lineEdit_autor.setText(_translate("Dialog", "KIM JONG-UN", None))
        self.label_comentarios.setText(_translate("Dialog", "Comentarios:", None))
        self.plainTextEdit_comentarios.setPlainText(_translate("Dialog", "No comments.", None))
        self.pushButton_aceptar.setText(_translate("Dialog", "&Aceptar", None))
        self.pushButton_cancelar.setText(_translate("Dialog", "&Cancelar", None))

