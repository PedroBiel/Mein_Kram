# -*- coding: utf-8 -*-
"""
DESCRIPCIÓN

Created on Wed Dec  4 12:02:03 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd


class DPernosDF():
    """
    Crea el DataFrame con los datos necesarios del diámetro de los pernos para
    mostrar en QTableView.
    """

    def __init__(self, d, As):
        self.d = d  # Diámetro del perno.
        self.As = As  # Área de tensión del perno de anclaje.

    def dataframe_diametro_pernos(self):
        """DataFrame."""

        df_n_pernos = pd.DataFrame(
                {'Símbolo': [
                        'd',
                        'A.s'
                        ],
                 'Magnitud': [
                         self.d,
                         self.As
                         ],
                 'Unidades': [
                         'mm',
                         'cm²'
                         ],
                 'Definición': [
                         'Diámetro',
                         'Área de tensión'
                         ],
                 'Norma/Estándar': [
                         '',
                         ''
                         ]
                 })

        return df_n_pernos
