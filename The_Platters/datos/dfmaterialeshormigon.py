# -*- coding: utf-8 -*-
"""
Obtiene del DataFrame de la base de datos SQLite los datos necesarios

Created on Wed Dec 11 07:47:50 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd


class DFMaterialPlaca:
    """
    Obtiene del DataFrame de la base de datos SQLite los datos necesarios.
    """

    def __init__(self, df, material):
        self.df = df  # DataFrame de la base de datos SQLite.
        self.material = material  # Calidad del material.

    def norma(self):
        """Norma."""

        norma = self.df['Norma'].loc[
                (self.df['Calidad'] == self.material)
                ].item()

        return norma

    def calidad(self):
        """Calidad."""

        calidad = self.df['Calidad'].loc[
                (self.df['Calidad'] == self.material)
                ].item()

        return calidad

    def resistencia_caracteristica_compresion(self):
        """
        Resistencia característica a compresión del hormigón sobre probeta
        cilíndrica a los 28 días.
        """

        fck = self.df['fck'].loc[
                (self.df['Calidad'] == self.material)
                ].item()

        return fck

    def valor_medio_resistencia_compresión(self):
        """
        Valor medio de la resistencia a compresión del hormigón sobre probeta
        cilíndrica.
        """

        fcm = self.df['fcm'].loc[
                (self.df['Calidad'] == self.material)
                ].item()

        return fcm


class MaterialHormigonDF(DFMaterialPlaca):
    """
    Crea el DataFrame con los datos necesarios del hormigón para mostrar en
    QTableView.
    """

    def __init__(self, df, nominal):
        DFMaterialPlaca.__init__(self, df, nominal)
        self.norma = DFMaterialPlaca.norma(self)
        self.calidad = DFMaterialPlaca.calidad(self)
        self.fck = DFMaterialPlaca.resistencia_caracteristica_compresion(self)
        self.fcm = DFMaterialPlaca.valor_medio_resistencia_compresión(self)

    def dataframe_material_hormigon(self):
        """DataFrame."""

        df_material_hormigon = pd.DataFrame(
                {'Símbolo': [
                        'HORMIGÓN',
                        self.calidad,
                        'f.ck',
                        'f.cm'
                        ],
                 'Magnitud': [
                         '',
                         '',
                         self.fck,
                         self.fcm
                         ],
                 'Unidades': [
                         '',
                         '',
                         'MPa',
                         'MPa'
                         ],
                 'Definición': [
                         '',
                         'Denominación',
                         'Resistencia característica a compresión',
                         'Valor medio de la resistencia a compresión'
                         ],
                 'Norma/Estándar': [
                         '',
                         self.norma,
                         self.norma,
                         self.norma,
                         ]
                 })

        return df_material_hormigon
