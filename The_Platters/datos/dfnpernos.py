# -*- coding: utf-8 -*-
"""
Obtiene del DataFrame con los datos necesarios

Created on Wed Dec  4 09:23:51 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd


class NPernosDF():
    """
    Crea el DataFrame con los datos necesarios del nº de pernos para mostrar en
    QTableView.
    """

    def __init__(self, n_pernos):
        self.n_pernos = n_pernos  # Nº de pernos.

    def dataframe_numero_pernos(self):
        """DataFrame."""

        df_n_pernos = pd.DataFrame(
                {'Símbolo': [
                        'PERNOS DE ANCLAJE',
                        'Nº de pernos y posición'
                        ],
                 'Magnitud': [
                         '',
                         self.n_pernos
                         ],
                 'Unidades': [
                         '',
                         ''
                         ],
                 'Definición': [
                         '',
                         ''
                         ],
                 'Norma/Estándar': [
                         '',
                         ''
                         ]
                 })

        return df_n_pernos
