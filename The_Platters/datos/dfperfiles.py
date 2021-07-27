# -*- coding: utf-8 -*-
"""
Obtiene del DataFrame de la base de datos SQLite los datos necesarios

Created on Wed Nov 27 11:20:08 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd


class DFPerfil:
    """
    Obtiene del DataFrame de la base de datos SQLite los datos necesarios.
    """

    def __init__(self, df, nominal):
        self.df = df  # DataFrame de la base de datos SQLite.
        self.nominal = nominal  # Valor nominal del perfil.

    def perfil(self):
        """Perfil."""

        perfil = self.df['Perfil'].loc[
            self.df['nominal'] == self.nominal
            ].values.item()

        return str(perfil)

    def canto(self):
        """Canto del perfil."""

        h = self.df['h_mm'].loc[
            self.df['nominal'] == self.nominal
            ].values.item()

        return h

    def ancho(self):
        """Ancho del perfil."""

        b = self.df['b_mm'].loc[
            self.df['nominal'] == self.nominal
            ].values.item()

        return b

    def espesor_alma(self):
        """Espesor del alma del perfil."""

        tw = self.df['tw_mm'].loc[
            self.df['nominal'] == self.nominal
            ].values.item()

        return tw

    def espesor_ala(self):
        """Espesor del ala del perfil."""

        tf = self.df['tf_mm'].loc[
            self.df['nominal'] == self.nominal
            ].values.item()

        return tf


class PerfilDF(DFPerfil):
    """
    Crea el DataFrame con los datos necesarios de los perfiles para mostrar en
    QTableView.
    """

    def __init__(self, df, nominal):
        DFPerfil.__init__(self, df, nominal)
        self.perfil = DFPerfil.perfil(self)
        self.h = DFPerfil.canto(self)
        self.b = DFPerfil.ancho(self)
        self.tw = DFPerfil.espesor_alma(self)
        self.tf = DFPerfil.espesor_ala(self)

    def dataframe_perfil(self):
        """DataFrame."""

        df_perfil = pd.DataFrame(
                {'Símbolo': [
                        'PERFIL',
                        self.perfil,
                        'h',
                        'b',
                        't.w',
                        't.f'
                        ],
                 'Magnitud': [
                         '',
                         self.nominal,
                         self.h,
                         self.b,
                         self.tw,
                         self.tf
                         ],
                 'Unidades': [
                         '',
                         '',
                         'mm',
                         'mm',
                         'mm',
                         'mm'
                         ],
                 'Definición': [
                         '',
                         '',
                         'Canto',
                         'Ancho',
                         'Espesor del alma',
                         'Espesor del ala'
                         ],
                 'Norma/Estándar': [
                         '',
                         '',
                         '',
                         '',
                         '',
                         ''
                         ]
                 })

        return df_perfil
