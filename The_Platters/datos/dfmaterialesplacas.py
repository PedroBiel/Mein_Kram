# -*- coding: utf-8 -*-
"""
Obtiene del DataFrame de la base de datos SQLite los datos necesarios

Created on Wed Dec  4 14:15:25 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd


class DFMaterialPlaca:
    """
    Obtiene del DataFrame de la base de datos SQLite los datos necesarios.
    """

    def __init__(self, d, df, material):
        # Habrá que sustituir self.v.d por self.v.tp ###############
        from math import ceil
        self.tp = ceil(d / 5) * 5  # Espesor de la placa base.
        self.df = df  # DataFrame de la base de datos SQLite.
        self.material = material  # Calidad del material y espesor máximo.

        self.df_mat = self.df[self.df['Calidad'] == self.material]
        self.t = self.df_mat.loc[self.df_mat['tmax'] >= self.tp, 'tmax'].min()

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


class MaterialPlacaDF(DFMaterialPlaca):
    """
    Crea el DataFrame con los datos necesarios de los materiles para mostrar en
    QTableView.
    """

    def __init__(self, d, df, material):
        DFMaterialPlaca.__init__(self, d, df, material)
        self.norma = DFMaterialPlaca.norma(self)
        self.calidad = DFMaterialPlaca.calidad(self)
        self.tmax = DFMaterialPlaca.espesor_max(self)
        self.fy = DFMaterialPlaca.limite_elastico(self)
        self.fu = DFMaterialPlaca.tension_rotura(self)

    def dataframe_material_placa(self):
        """DataFrame."""

        df_material_perno = pd.DataFrame(
                {'Símbolo': [
                        'MATERIAL DE LA PLACA BASE',
                        self.calidad,
                        't.max',
                        'f.yp',
                        'f.up'
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


