# -*- coding: utf-8 -*-
"""
Obtiene del DataFrame de la base de datos SQLite los datos necesarios

Created on Wed Dec  4 08:41:11 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd


class DFMaterialPerno:
    """
    Obtiene del DataFrame de la base de datos SQLite los datos necesarios.
    """

    def __init__(self, d, df, material):
        self.d = d  # Diámetro del perno.
        self.df = df  # DataFrame de la base de datos SQLite.
        self.material = material  # Calidad del material y espesor máximo.

        self.df_mat = self.df[self.df['Calidad'] == self.material]
        self.t = self.df_mat.loc[self.df_mat['tmax'] >= self.d, 'tmax'].min()

    def norma(self):
        """Norma."""

        norma = self.df_mat['Norma'].loc[
                (self.df_mat['tmax'] == self.t)
                ].item()

        return norma

    def calidad(self):
        """Calidad."""

        calidad = self.df_mat['Calidad'].loc[
                (self.df_mat['tmax'] == self.t)
                ].item()

        return calidad

    def espesor_max(self):
        """Espesro máximo."""

        tmax = self.df_mat['tmax'].loc[
                (self.df_mat['tmax'] == self.t)
                ].item()

        return tmax

    def limite_elastico(self):
        """Límite elástico."""

        fy = self.df_mat['fy'].loc[
                (self.df_mat['tmax'] == self.t)
                ].item()

        return fy

    def tension_rotura(self):
        """Límite de rotura."""

        fu = self.df_mat['fu'].loc[
                (self.df_mat['tmax'] == self.t)
                ].item()

        return fu


class MaterialPernoDF(DFMaterialPerno):
    """
    Crea el DataFrame con los datos necesarios de los materiles para mostrar en
    QTableView.
    """

    def __init__(self, d, df, material):
        DFMaterialPerno.__init__(self, d, df, material)
        self.norma = DFMaterialPerno.norma(self)
        self.calidad = DFMaterialPerno.calidad(self)
        self.tmax = DFMaterialPerno.espesor_max(self)
        self.fy = DFMaterialPerno.limite_elastico(self)
        self.fu = DFMaterialPerno.tension_rotura(self)

    def dataframe_material_perno(self):
        """DataFrame."""

        df_material_perno = pd.DataFrame(
                {'Símbolo': [
                        'MATERIAL DEL PERNO',
                        self.calidad,
                        't.max',
                        'f.yb',
                        'f.ub'
                        ],
                 'Magnitud': [
                         '',
                         '',
                         self.tmax,
                         self.fy,
                         self.fu
                         ],
                 'Unidades': [
                         '',
                         '',
                         'mm',
                         'MPa',
                         'MPa',
                         ],
                 'Definición': [
                         '',
                         '',
                         'Espesor máximo',
                         'Límite elástico',
                         'Tensión de rotura',
                         ],
                 'Norma/Estándar': [
                         '',
                         self.norma,
                         self.norma,
                         self.norma,
                         self.norma,
                         ]
                 })

        return df_material_perno
