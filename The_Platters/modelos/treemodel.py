# -*- coding: utf-8 -*-
"""
DESCRIPCIÓN

Created on Wed Nov 20 11:04:22 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


from PyQt5.QtGui import QStandardItem


class TreeModel:

    def rellenar_recursivo(self, data, padre):

        if type(data) == list:

            for elemento in data:

                padre.appendRow(QStandardItem(elemento))
                padre.setEditable(False)

        else:

            for clave, valor in data.items():

                hijo = QStandardItem(clave)
                hijo.setEditable(False)
                padre.appendRow(hijo)
                padre.setEditable(False)
                self.rellenar_recursivo(valor, hijo)
