# -*- coding: utf-8 -*-
"""
Obtiene del DataFrame de la base de datos SQLite los datos necesarios

Created on Fri Nov 29 13:46:38 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd


class DFMaterial:
    """
    Obtiene del DataFrame de la base de datos SQLite los datos necesarios.
    """

    def __init__(self, df_perfil, df, material):
        self.df_perfil = df_perfil  # DataFrame con los datos del perfil.
        self.df = df  # DataFrame de la base de datos SQLite.
        self.material = material  # Calidad del material y espesor máximo.

        tw = df_perfil.loc[df_perfil['Símbolo'] == 't.w', 'Magnitud'].item()
        tf = df_perfil.loc[df_perfil['Símbolo'] == 't.f', 'Magnitud'].item()
        tmax = max(tw, tf)

        self.df_mat = self.df[self.df['Calidad'] == self.material]
        self.t = self.df_mat.loc[self.df_mat['tmax'] >= tmax, 'tmax'].min()

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


class MaterialDF(DFMaterial):
    """
    Crea el DataFrame con los datos necesarios de los materiles para mostrar en
    QTableView.
    """

    def __init__(self, df_perfil, df, material):
        DFMaterial.__init__(self, df_perfil, df, material)
        self.norma = DFMaterial.norma(self)
        self.calidad = DFMaterial.calidad(self)
        self.tmax = DFMaterial.espesor_max(self)
        self.fy = DFMaterial.limite_elastico(self)
        self.fu = DFMaterial.tension_rotura(self)

    def dataframe_material(self):
        """DataFrame."""

        df_material = pd.DataFrame(
                {'Símbolo': [
                        'MATERIAL DEL PERFIL',
                        self.calidad,
                        't.max',
                        'f.y',
                        'f.u'
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

        return df_material
