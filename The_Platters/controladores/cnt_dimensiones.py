# -*- coding: utf-8 -*-
"""
THE PLATTERS, el generador de placas base TW
Controlador Dimensiones

Created on Wed Dec 11 10:32:41 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""

import pandas as pd

from datos.dimensiones import Dimensiones
from datos.dfdimensiones import DimensionesDF
from datos.listadf import ListaDF


class CntDimensiones:
    """Controlador de dimensiones de la placa base."""

    def __init__(self, ventana):
        self.v = ventana

    def placa_base(self):
        self.obten_dimensiones()
        self.df_datos_dimensiones()
        self.df_concat()
        self.v.table_model_dimensiones()

    def obten_dimensiones(self):
        """Dimensiones de la placa base."""

        dimensiones = Dimensiones(
                self.v.d,
                self.v.df_perfil,
                self.v.df_perfiles,
                self.v.n_pernos
                )
        self.v.h = dimensiones.canto_perfil()
        self.v.b = dimensiones.ancho_perfil()
        self.v.tw = dimensiones.espesor_alma_perfil()
        self.v.tf = dimensiones.espesor_ala_perfil()
        self.v.mn = dimensiones.mortero_nivelacion()
        self.v.d0 = dimensiones.diametro_taladro()
        self.v.m = dimensiones.entre_taladro_superficie()
        self.v.w = dimensiones.entre_taladros_w()
        self.v.p = dimensiones.entre_taladros_p()
        self.v.tp = dimensiones.espesor_placa_base()
        self.v.e = dimensiones.entre_taladro_borde()
        self.v.hp = dimensiones.canto_placa_base()
        self.v.bp = dimensiones.ancho_placa_base()

    def df_datos_dimensiones(self):
        """DataFrame con los datos de las dimensiones."""

        dimensiones_df = DimensionesDF(
                self.v.hp,
                self.v.bp,
                self.v.tp,
                self.v.w,
                self.v.p,
                self.v.d0,
                self.v.mn
                )
        self.v.df_dimensiones = dimensiones_df.dataframe_dimensiones()

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
