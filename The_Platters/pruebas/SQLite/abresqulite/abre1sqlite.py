# -*- coding: utf-8 -*-
"""
Abre una base de datos SQLite y la muestra en un árbol.

Created on Fri Nov 15 13:44:39 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import qdarkstyle
import sys

from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView

from controladores.cnt_abresqlite import CntAbreSqlite


class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        uic.loadUi('vistas/abresqlite.ui', self)

        self.cnt_abre_sqlite = CntAbreSqlite(self)

        self.btn_abre_sqlite = self.pushButton_abrir_sqlite
        self.filtro = self.lineEdit_filtro
        self.tre_sqlite = self.treeView_sqlite
        self.log = self.textEdit_log
        self.log.setCurrentFont(QFont('Consolas', 8))

        self.view = QTreeView()

        self.btn_abre_sqlite.clicked.connect(self.cnt_abre_sqlite.abre_sqlite)
        self.tre_sqlite.clicked.connect(self.cnt_abre_sqlite.tree_item)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
