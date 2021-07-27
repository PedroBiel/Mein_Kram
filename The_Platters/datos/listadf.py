# -*- coding: utf-8 -*-
"""
THE PLATTERS, el generador de placas base TW
Lista con los DataFrames para mostrar en el QTableView

Created on Wed Dec 18 12:25:20 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


class ListaDF:
    """Lista con los DataFrames para mostrar en el QTableView."""

    def __init__(self, *args):
        self.args = args

    def lista_df(self):
        lista = [
                self.args[0][0],
                self.args[0][1],
                self.args[0][2],
                self.args[0][3],
                self.args[0][4],
                self.args[0][5],
                self.args[0][6],
                self.args[0][7]
                ]

        return lista
