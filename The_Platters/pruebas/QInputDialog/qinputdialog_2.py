# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QInputDialog,       QWidget, QListWidgetItem   # ++

class Ui_Dialog(QWidget):                                 # - object  + QWidget

    def Addlist(self):
        self.listWidget.addItem(self.lineEdit.text())
        self.lineEdit.setText('')
        self.lineEdit.setFocus()

    def Editlist(self):
        row = self.listWidget.currentRow()
        newtext, ok = QInputDialog.getText(self, "Enter new text", "Enter new text")  

        if ok and (len(newtext) !=0):
            self.listWidget.takeItem(self.listWidget.currentRow())
            self.listWidget.insertItem(row, QListWidgetItem(newtext)) 

    def Delete(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def Deleteall(self):
        self.listWidget.clear()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(570, 318)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.AddButton = QtWidgets.QPushButton(Dialog)
        self.AddButton.setGeometry(QtCore.QRect(150, 80, 75, 23))
        self.AddButton.setObjectName("AddButton")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(290, 20, 256, 271))
        self.listWidget.setObjectName("listWidget")
        self.EditButton = QtWidgets.QPushButton(Dialog)
        self.EditButton.setGeometry(QtCore.QRect(150, 120, 75, 23))
        self.EditButton.setObjectName("EditButton")
        self.DeteleButton = QtWidgets.QPushButton(Dialog)
        self.DeteleButton.setGeometry(QtCore.QRect(150, 160, 75, 23))
        self.DeteleButton.setObjectName("DeteleButton")
        self.DeleteAllButton = QtWidgets.QPushButton(Dialog)
        self.DeleteAllButton.setGeometry(QtCore.QRect(150, 200, 75, 23))
        self.DeleteAllButton.setObjectName("DeleteAllButton")
        self.listWidget.addItem('Pizza')
        self.listWidget.addItem('Pasta')
        self.listWidget.addItem('Burrito')
        self.listWidget.addItem('Hamburger')
        self.AddButton.clicked.connect(self.Addlist)
        self.EditButton.clicked.connect(self.Editlist)
        self.DeteleButton.clicked.connect(self.Delete)
        self.DeleteAllButton.clicked.connect(self.Deleteall)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Text"))
        self.AddButton.setText(_translate("Dialog", "Add"))
        self.EditButton.setText(_translate("Dialog", "Edit"))
        self.DeteleButton.setText(_translate("Dialog", "Delete"))
        self.DeleteAllButton.setText(_translate("Dialog", "Delete All"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

