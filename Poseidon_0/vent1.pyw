import sys

from PyQt4.QtCore import *
#from PyQt4.QtGui import *

from classes.EN_1998.EN_1998_0_0_171106 import EN_1998

from qtdesigner.ventana1 import *
from qtdesigner.ventana2 import *


class Window(QtGui.QMainWindow):

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.lineEdit_Ventana1 = self.ui.lineEdit_Ventana1

        # Abre Ventana2 desde menú.
        self.action_Ventana2 = self.ui.actionVentana_2
        self.action_Ventana2.setShortcut('Ctrl+V')
        self.action_Ventana2.setStatusTip('Abre la Ventana 2')
        self.action_Ventana2.triggered.connect(self.abre_ventana2)

        # Abre Ventana2 con el Botón.
        self.pushButton_Venatana2 = self.ui.pushButton_Ventana2

        # Abre Ventana 2
        QObject.connect(self.ui.pushButton_Ventana2, QtCore.SIGNAL('clicked()'), self.abre_ventana2)

    def abre_ventana2(self):

        self.lineEdit_Ventana1.setText('---')

        self.ventana2 = Ventana2(self)
        self.ventana2.ui.lineEdit_Ventana2.setText('xxx')
        self.ventana2.show()


class Ventana2(QtGui.QMainWindow):

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.window = Window(self)

        self.ventana2 = self.ui.lineEdit_Ventana2

        # Vuelve a Ventana 1
        self.pushButton_Ventana1 = self.ui.pushButton_Ventana1
        QObject.connect(self.pushButton_Ventana1, QtCore.SIGNAL('clicked()'), self.abre_ventana1)

    def abre_ventana1(self):

        self.hide()  # Cierra Ventana 2.

        self.ventana2.setText('---')
        self.window.lineEdit_Ventana1.setText('xxx')


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    myapp = Window()
    myapp.show()
    sys.exit(app.exec_())