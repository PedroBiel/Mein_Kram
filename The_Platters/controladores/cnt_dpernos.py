# -*- coding: utf-8 -*-
"""
THE PLATTERS, el generador de placas base TW
Controlador DPernos

Created on Mon Dec  2 13:57:48 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd

from datos.constantes import Constantes
from datos.dfdpernos import DPernosDF


class CntDPernos:
    """
    Controlador del diámetro de los pernos.
    """

    def __init__(self, ventana):
        self.v = ventana

    def lista_diametro_pernos(self):
        """Lista con el diámetro de los pernos."""

        self.lst_d_pernos = Constantes.d_pernos

        return self.lst_d_pernos

    def diametro_pernos_inicial(self):
        """Diámetro de los pernos inicial a iniciar la aplicación."""

        lst_d_pernos = self.lista_diametro_pernos()
        d_pernos = lst_d_pernos[0]

        return d_pernos

    # Obtén datos.
    # ------------
    def diametro_pernos(self):
        self.current_index = self.v.cbx_d_pernos.currentIndex()
        self.diametro()
        self.diametro_agujero()
        self.area()
        self.df_datos_diametro_pernos()
        self.df_concat()
        self.v.table_model_diametro_pernos()

    def diametro(self):
        """Diámetro del perno."""
    
        self.v.d = Constantes.d[self.current_index]  # [mm]

        return self.v.d

    def diametro_agujero(self):
        """Diámetro del agujero para el perno."""

        self.v.d0 = Constantes.d0[self.current_index]  # [mm]

        return self.v.d0

    def area(self):
        """Área de tensión del perno de anclaje."""

        self.v.As = Constantes.As[self.current_index]  # [cm²]

        return self.v.As

    def df_datos_diametro_pernos(self):
        """DataFrame con los datos del diámetro de los pernos."""

        dpernos_df = DPernosDF(self.v.d, self.v.As)
        self.v.df_dpernos = dpernos_df.dataframe_diametro_pernos()

        return self.v.df_dpernos

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











