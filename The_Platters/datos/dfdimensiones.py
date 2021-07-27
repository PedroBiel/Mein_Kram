# -*- coding: utf-8 -*-
"""
Obtiene del DataFrame de la base de datos SQLite los datos necesarios

Created on Fri Dec 13 13:13:10 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd


class DimensionesDF:
    """
    Crea el DataFrame con los datos necesarios de las dimensiones para mostrar
    en QTableView.
    """

    def __init__(self, hp, bp, tp, w, p, d0, mn):
        self.hp = hp
        self.bp = bp
        self.tp = tp
        self.w = w
        self.p = p
        self.d0 = d0
        self.mn = mn

    def dataframe_dimensiones(self):
        """DataFrame."""

        df_dimensiones = pd.DataFrame(
                {'Símbolo': [
                        'DIMENSIONES DE LA PLACA BASE',
                        'h.p',
                        'b.p',
                        't.p',
                        'w',
                        'p',
                        'd.0',
                        'MN'
                        ],
                 'Magnitud': [
                         '',
                         self.hp,
                         self.bp,
                         self.tp,
                         self.w,
                         self.p,
                         self.d0,
                         self.mn
                         ],
                 'Unidades': [
                         '',
                         'mm',
                         'mm',
                         'mm',
                         'mm',
                         'mm',
                         'mm',
                         'mm'
                         ],
                 'Definición': [
                         '',
                         'Canto',
                         'Ancho',
                         'Espesor',
                         'Separación entre taladros',
                         'Separación entre taladros',
                         'Diámetro del agujero',
                         'Espesor del mortero de nivelación'
                         ],
                 'Norma/Estándar': [
                         '',
                         '',
                         '',
                         '',
                         'EN 1993-1-8:2003',
                         'EN 1993-1-8:2003',
                         'CI-2-15',
                         'CI-2-15'
                         ]
                 })

        return df_dimensiones
