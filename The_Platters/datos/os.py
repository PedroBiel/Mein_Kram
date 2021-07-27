# -*- coding: utf-8 -*-
"""
DESCRIPCIÓN

Created on Tue Nov 26 09:08:27 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import os


class Os:

    def __init__(self, pfad, extension=''):
        self.pfad = pfad
        self.extension = extension

    def list_dir(self):
        """
        Devuelve una lista con los nombres de los ficheros en el directorio.
        """

        os.chdir(self.pfad)
        os.getcwd()
        list_dir = os.listdir(self.pfad)
        lista = [fichero for fichero in list_dir]

        return lista

    def list_dir_ext(self):
        """
        Devuelve una lista con los nombres de los ficheros en el directorio con
        una misma extensión.
        """

        os.chdir(self.pfad)
        os.getcwd()
        list_dir = os.listdir(self.pfad)
        lista = [fichero for fichero in list_dir if self.extension in fichero]

        return lista

    def list_dir_ext_oculta(self):
        """
        Devuelve una lista con los nombres de los ficheros en el directorio con
        una misma extensión ocultando la extensión en el nombre.
        """

        lista = []
        ln = len(self.extension)
        lista_con_extension = self.list_dir_ext()

        for nombre in lista_con_extension:

            if self.extension in nombre:

                lista.append(nombre[:-ln])

        return lista
