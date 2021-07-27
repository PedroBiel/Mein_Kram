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


class SQLites:
    """
    Bases de datos SQLite3.
    """

    def __init__(self, ruta_db, lista_db):
        self.ruta_db = ruta_db
        self.lista_db = lista_db

        self.dcc_db = {}  # Diccionario con ell nombre y las tablas de la base de datos SQLite.

    def diccionario_db(self):
        """
        Devuelve el diccionario con el nombre de las bases de datos y sus
        tablas.
        """

        for db in self.lista_db:
            lista_tablas_db = []
            ruta_nombre_db = self.ruta_db + '/' + db  # Ruta/nombre de la base de datos.
            nmbr_db = db[:-3]  # Nombre de la base de datos.

            # Crea objeto de conexión y cursos para ejecutar sentencias.
            try:
                con = sqlite3.connect(ruta_nombre_db)
                cur = con.cursor()

            except Error as e:
                print('Error \n', e)

            # Puebla el diccionario con el nombre de la base de datos y sus tablas.
            tablas = cur.execute(
                    "SELECT name FROM sqlite_master WHERE type='table';"
                    )

            for tabla in tablas:
                lista_tablas_db.append(tabla[0])

            self.dcc_db[nmbr_db] = lista_tablas_db
            con.close()

        return self.dcc_db
