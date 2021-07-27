# -*- coding: utf-8 -*-
"""
Dimensiones de la placa base

Created on Wed Dec 11 11:16:43 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


from math import ceil

from datos.constantes import Constantes


class Dimensiones:
    """Dimensiones de la placa base."""

    def __init__(self, d, df_perfil, df_perfiles, n_pernos):
        self.d = d  # Diámetro nominal del perno.
        self.df_perfil = df_perfil  # DataFrame con los datos del perfil.
        self.df_perfiles = df_perfiles  # DataFrame con los datos de los perfiles.
        self.n_pernos = n_pernos

        self.r_5 = Constantes.REDONDEO_5
        self.r_10 = Constantes.REDONDEO_10

        self.d0 = self.diametro_taladro()
        self.m = self.entre_taladro_superficie()
        self.tp = self.espesor_placa_base()

    def ancho_perfil(self):
        """Ancho del perfil."""

        b = self.df_perfil['Magnitud'].loc[
                self.df_perfil['Símbolo'] == 'b'
                ].values.item()

        return b

    def ancho_placa_base(self):
        """Ancho de la placa base."""

        b = self.ancho_perfil()
        e = self.entre_taladro_borde()
        m = self.entre_taladro_superficie()
        w = self.entre_taladros_w()

        if (
                self.n_pernos == '2 pernos int.') or (
                self.n_pernos == '4 pernos int.'
                ):
            bp1 = 2 * e + w
            bp2 = b + 40
            bp = max(bp1, bp2)

        elif self.n_pernos == '6 pernos; 2 int, 4 ext.':

            bp = b + 2 * (m + e)

        bp = ceil(bp / self.r_10) * self.r_10

        return bp

    def canto_placa_base(self):
        """Canto de la placa base."""

        h = self.canto_perfil()
        idx = self.df_perfiles.h_mm[
                self.df_perfiles.h_mm == h
                ].index.values.astype(int)[0]

        if h <= 600:
            hp = self.df_perfiles.iloc[idx + 3, 3]

        else:
            hp = h + 100

        hp = ceil(hp / self.r_10) * self.r_10

        return hp

    def canto_perfil(self):
        """Canto del perfil."""

        h = self.df_perfil['Magnitud'].loc[
                self.df_perfil['Símbolo'] == 'h'
                ].values.item()

        return h

    def diametro_taladro(self):
        """Diámetro del taladro de un perno."""

        lista_d = Constantes.d
        lista_d0 = Constantes.d0

        idx = lista_d.index(self.d)
        d0 = lista_d0[idx]

        return d0

    def entre_taladro_superficie(self):
        """Distancia del eje del taladro a la superficie paralela."""

        m = 3 * self.d

        return m

    def espesor_ala_perfil(self):
        """Espesor del ala del perfi."""

        tf = self.df_perfil['Magnitud'].loc[
                self.df_perfil['Símbolo'] == 't.f'
                ].values.item()

        return tf

    def espesor_alma_perfil(self):
        """Espesor del alma del perfi."""

        tw = self.df_perfil['Magnitud'].loc[
                self.df_perfil['Símbolo'] == 't.w'
                ].values.item()

        return tw

    def espesor_placa_base(self):
        """Espesor de la placa base."""

        tp = ceil(self.d / self.r_5) * self.r_5

        return tp

    def entre_taladro_borde(self):
        """Separación entre el centro del taladro y el borde adyacente."""

        tp = self.espesor_placa_base()
        
        emin = 1.2 * self.d0
        emax = 4 * tp + 40
        e = (emin + emax) / 2
        e = ceil(e / self.r_10) * self.r_10

        return e

    def entre_taladros_p(self):
        """Separación entre taladros."""

        h = self.canto_perfil()
        tf = self.espesor_ala_perfil()
        m = self.entre_taladro_superficie()
        tp = self.espesor_placa_base()

        if self.n_pernos == '2 pernos int.':
            # No hay separación p.
            p = 0

        elif self.n_pernos == '4 pernos int.':
            pmin = 2.2 * self.d0
            pmax1 = 14 * tp
            pmax2 = 200
            pmax = min(pmax1, pmax2)
            p = (pmin + pmax) / 2

            # Validación de la separación entre taladros w.
            # ---------------------------------------------
            # Hay que comprobar que el espacio entre las alas del perfil es
            # suficiente para alojar los pernos. Si no es el caso, se
            # desestiman los cuatro pernos.
            if p > h - 2 * (tf + m):
                p = 0

        elif self.n_pernos == '4 pernos ext.':
            p = h + 2 * m

        elif self.n_pernos == '6 pernos; 2 int, 4 ext.':
            p = h + 2 * m

        p = ceil(p / self.r_10) * self.r_10

        return p

    def entre_taladros_w(self):
        """Separación entre taladros."""

        b = self.ancho_perfil()
        h = self.canto_perfil()
        tw = self.espesor_alma_perfil()
        w = 2 * self.m + tw
        m = self.entre_taladro_superficie()

        # Validación de la separación entre taladros w.
        # ---------------------------------------------
        # Si el agujero del taladro del perno queda dentro del espacio de las
        # alas del perfil, hay que comprobar que hay espacio suficiente entre
        # las alas del perfil para alojar el perno. Si no es el caso, la
        # separación mínima será la mitad del ancho del ala del perfil.
        if (b / 2 > m) and (h < 2 * m):
            w = b

        w = ceil(w / self.r_10) * self.r_10

        return w

    def mortero_nivelacion(self):
        """Espesor del mortero de nivelación."""

        lista_d = Constantes.d
        lista_mn = Constantes.mn

        idx = lista_d.index(self.d)
        mn = lista_mn[idx]

        return mn
