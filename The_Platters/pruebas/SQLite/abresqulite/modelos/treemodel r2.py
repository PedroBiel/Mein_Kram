# -*- coding: utf-8 -*-
"""
DESCRIPCIÓN

Created on Fri Nov 22 09:19:04 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import sys

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QTreeView


datos = {
    "América": {
        "Argentina": ['Buenos Aires', 'Córdoba'],
        "Colombia":  ['Bogotá', 'Cali'],
        "Méjico":    ['Ciudad de Méjico', 'Guadalajara']
    },
    "Europa": {
        "España":    ['Madrid'],
        "Francia":   ['París']
    }
}


def rellenar_recursivo(data, padre):
    if type(data) == list:
        for elemento in data:
            padre.appendRow(QStandardItem(elemento))
    else:
        for clave, valor in data.items():
            hijo = QStandardItem(clave)
            padre.appendRow(hijo)
            rellenar_recursivo(valor, hijo)


app = QApplication(sys.argv)
model = QStandardItemModel()
view = QTreeView(headerHidden=True)
view.setModel(model)

rellenar_recursivo(datos, model.invisibleRootItem())
view.show()
app.exec_()
