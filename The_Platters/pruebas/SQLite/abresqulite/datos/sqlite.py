# -*- coding: utf-8 -*-
"""
SQLite library
https://docs.python.org/3.8/library/sqlite3.html

Created on Mon Nov 18 11:08:30 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import sqlite3

from sqlite3 import Error


class SQLite:
    """
    Base de datos SQLite3.
    """

    def __init__(self, ruta_nombre_db):
        self.ruta_nombre_db = ruta_nombre_db

        self.cur = ''  # Objeto cursor para ejecutar sentencias de SQLite.
        self.nmbr_db = ''  # Nombre de la base de datos SQLite.
        self.lista_tablas_db = []  # Lista con las tablas de la base de datos SQLite.
        self.dcc_db = {}  # Diccionario con ell nombre y las tablas de la base de datos SQLite.

    def conecta_cursor(self):
        """
        Crea un objeto de conexión para conectar a la base de datos y un cursor
        para ejecutare las sentencias.
        """
        try:
            con = sqlite3.connect(self.ruta_nombre_db)
            self.cur = con.cursor()
        except Error as e:
            print('Error \n', e)
#        finally:
#            con.close()

    def nombre_db(self):
        """Devuelve el nombre de la base de datos SQLite."""

        idx = self.ruta_nombre_db.rfind('/')
        self.nmbr_db = self.ruta_nombre_db[idx + 1:-3]

        return self.nmbr_db

    def tablas_db(self):
        """Devuelve la lista con las tablas de la base de datos SQLite."""

        self.conecta_cursor()
        tablas = self.cur.execute(
                "SELECT name FROM sqlite_master WHERE type='table';"
                )
        for tabla in tablas:
            self.lista_tablas_db.append(tabla[0])

        return self.lista_tablas_db

    def diccionario_db(self):
        """
        Devuelve el diccionario con el nombre de la base de datos y sus tablas.
        """

        self.dcc_db[self.nmbr_db] = self.lista_tablas_db

        return self.dcc_db
