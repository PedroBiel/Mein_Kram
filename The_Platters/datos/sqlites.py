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

    def __init__(self, ruta_db, lista_db, tabla):
        self.ruta_db = ruta_db
        self.lista_db = lista_db
        self.tabla = tabla

        self.dcc_db = {}  # Diccionario con el nombre y las tablas de la base de datos SQLite.
        self.lst_dbs = []  # Lista con las bases de datos.
        self.lst_lst_tablas = []  # Lista con las listas de las tablas.
        self.lst_val_tablas = []  # Lista con las listas de los valores de las tablas.

    def diccionario_db_tbl(self):
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

    def diccionario_db_tbl_val(self):
        """
        Devuelve el diccionario con el nombre de las bases de datos, sus
        tablas y los valores de las tablas.
        """

        self.listas_db()

        for db, lst_tablas, val_tablas in zip(
                self.lst_dbs,
                self.lst_lst_tablas,
                self.lst_val_tablas
                ):

            dcc_tablas = {}
        
            for tabla, val in zip(lst_tablas, val_tablas):
                dcc_tablas[tabla] = val
        
            self.dcc_db[db] = dcc_tablas
        
        return self.dcc_db

    def listas_db(self):
        """
        Devuelve las listas de las bases de datos, de las tablas y de los
        valores de las tablas.
        """

        for db in self.lista_db:
            ruta_nombre_db = self.ruta_db + '/' + db  # Ruta/nombre de la base de datos.
            nombre_db = db[:-3]  # Nombre de la base de datos.
            self.lst_dbs.append(nombre_db)

            # Crea objeto de conexión y cursos para ejecutar sentencias.
            try:
                con = sqlite3.connect(ruta_nombre_db)
                cur = con.cursor()
            except Error as e:
                print('Error \n', e)

            tablas = cur.execute(
                    "SELECT name FROM sqlite_master WHERE type='table';"
                    )  # Tablas en la base de datos..
            lst_tablas = []  # Lista temporal con los valores de las tablas.
            lst_val_tabla = []  # Lista con las listas de los valores de la tabla.

            for tabla in tablas:

                cur = con.cursor()
                cur.execute("SELECT " + self.tabla + " FROM " + tabla[0] + ";")
                rows = cur.fetchall()  # Filas de las tablas.

                lst_tablas.append(tabla[0])
                lst_nominal = []

                for row in rows:
                    lst_nominal.append(row[0])  # Añade filas a la lista.

                lst_nominal = list(dict.fromkeys(lst_nominal))  # Elimina duplicados.
                lst_val_tabla.append(lst_nominal)

            self.lst_val_tablas.append(lst_val_tabla)
            self.lst_lst_tablas.append(lst_tablas)

            con.close()
