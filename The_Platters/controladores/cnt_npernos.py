# -*- coding: utf-8 -*-
"""
THE PLATTERS, el generador de placas base TW
Controlador NPernos

Created on Mon Dec  2 12:40:50 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd

from datos.constantes import Constantes
from datos.dfnpernos import NPernosDF


class CntNPernos:
    """
    Controlador del número de pernos.
    """

    def __init__(self, ventana):
        self.v = ventana

    def lista_numero_pernos(self):
        """Lista con el nº de pernos y su posición."""

        self.lst_n_pernos = Constantes.n_pernos

        return self.lst_n_pernos

#    def numero_pernos_inicial(self):
#        """Nº de pernos inicial al iniciar la aplicación."""
#
#        lst_n_pernos = self.lista_numero_pernos()
#        self.v.n_pernos = lst_n_pernos[0]
#
#        return self.v.n_pernos

    # Obtén datos.
    # ------------
    def numero_pernos(self):
        self.n_pernos()
        self.df_datos_numero_pernos()
        self.df_concat()
        self.v.table_model_numero_pernos()

    def n_pernos(self):
        """Nº de pernos."""

#        if self.v.n_pernos == '':
#            self.v.n_pernos = self.numero_pernos_inical()

        current_index = self.v.cbx_n_pernos.currentIndex()
        self.v.n_pernos = self.v.cbx_n_pernos.itemText(current_index)

        return self.v.n_pernos

    def df_datos_numero_pernos(self):
        """DataFrame con los datos del nº de pernos."""

        npernos_df = NPernosDF(self.v.n_pernos)
        self.v.df_npernos = npernos_df.dataframe_numero_pernos()

        return self.v.df_npernos

    def df_concat(self):
        """Concatena el DataFrame actual con los anteriores."""

        lista = [
                self.v.df_perfil,
                self.v.df_material,
                self.v.df_npernos,
                self.v.df_dpernos,
                self.v.df_material_perno,
                self.v.df_material_placa,
                self.v.df_material_hormigon,
                self.v.df_dimensiones
                ]
        self.v.df = pd.concat(lista)

        return self.v.df
