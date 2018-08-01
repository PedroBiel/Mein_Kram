# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_propiedades.ui'
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
        Dialog.resize(370, 168)
        self.formLayout_2 = QtGui.QFormLayout(Dialog)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_cuadro = QtGui.QLabel(Dialog)
        self.label_cuadro.setObjectName(_fromUtf8("label_cuadro"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_cuadro)
        self.comboBox_cuadro = QtGui.QComboBox(Dialog)
        self.comboBox_cuadro.setEditable(True)
        self.comboBox_cuadro.setObjectName(_fromUtf8("comboBox_cuadro"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_cuadro)
        self.label_idioma = QtGui.QLabel(Dialog)
        self.label_idioma.setObjectName(_fromUtf8("label_idioma"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_idioma)
        self.comboBox_idioma = QtGui.QComboBox(Dialog)
        self.comboBox_idioma.setEditable(True)
        self.comboBox_idioma.setObjectName(_fromUtf8("comboBox_idioma"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_idioma)
        self.label_redondeo = QtGui.QLabel(Dialog)
        self.label_redondeo.setObjectName(_fromUtf8("label_redondeo"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_redondeo)
        self.comboBox_redondeo = QtGui.QComboBox(Dialog)
        self.comboBox_redondeo.setEditable(True)
        self.comboBox_redondeo.setObjectName(_fromUtf8("comboBox_redondeo"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_redondeo)
        self.label_filas_columnas = QtGui.QLabel(Dialog)
        self.label_filas_columnas.setObjectName(_fromUtf8("label_filas_columnas"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_filas_columnas)
        self.comboBox_filas_columnas = QtGui.QComboBox(Dialog)
        self.comboBox_filas_columnas.setEditable(True)
        self.comboBox_filas_columnas.setObjectName(_fromUtf8("comboBox_filas_columnas"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox_filas_columnas)
        self.formLayout_2.setLayout(1, QtGui.QFormLayout.LabelRole, self.formLayout)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(12, 25, 77, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(12, 48, 57, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(100, 20, 101, 81))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.checkBox = QtGui.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(11, 4, 37, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(11, 27, 37, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(11, 50, 36, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_aceptar = QtGui.QPushButton(Dialog)
        self.pushButton_aceptar.setObjectName(_fromUtf8("pushButton_aceptar"))
        self.horizontalLayout.addWidget(self.pushButton_aceptar)
        self.pushButton_cancelar = QtGui.QPushButton(Dialog)
        self.pushButton_cancelar.setObjectName(_fromUtf8("pushButton_cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_cancelar)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.LabelRole, self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Propiedades del cuadro de implantación", None))
        self.label_cuadro.setText(_translate("Dialog", "Cuadro para:", None))
        self.label_idioma.setText(_translate("Dialog", "Idioma:", None))
        self.label_redondeo.setText(_translate("Dialog", "Redondeo:", None))
        self.label_filas_columnas.setText(_translate("Dialog", "Filas/Columnas:", None))
        self.groupBox.setTitle(_translate("Dialog", "Momentos", None))
        self.radioButton.setText(_translate("Dialog", "Automático", None))
        self.radioButton_2.setText(_translate("Dialog", "Manual", None))
        self.checkBox.setText(_translate("Dialog", "Mx", None))
        self.checkBox_2.setText(_translate("Dialog", "My", None))
        self.checkBox_3.setText(_translate("Dialog", "Mz", None))
        self.pushButton_aceptar.setText(_translate("Dialog", "&Aceptar", None))
        self.pushButton_cancelar.setText(_translate("Dialog", "&Cancelar", None))

