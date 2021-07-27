# -*- coding: utf-8 -*-
"""
Conecta con base de datos SQLite y transfiere los datos a un pandas DataFrame

Created on Wed Nov 27 10:22:58 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd
import sqlite3

from PyQt5.QtWidgets import QInputDialog

from datos.qinputdialog import InputDialogGetItem


class SQLitePandasDF:
    """
    Conecta con base de datos SQLite y transfiere los datos de una tabla
    conocida a un pandas DataFrame.
    """

    def __init__(self, ruta, base_datos, tabla):
        self.ruta = ruta  # Ruta donde se encuentra la base de datos.
        self.base_datos = base_datos  # Nombre de la base de datos sin extensión.
        self.tbl = tabla  # Tabla de la base de datos.

    def conecta(self):
        try:
            self.db = self.ruta + '/' + self.base_datos + '.db'
            conn = sqlite3.connect(self.db)
            df_db = pd.read_sql('SELECT * FROM ' + self.tbl + ';', conn)
        except Exception as e:
            print('\n Seleccionar un perfil en el árbol,', str(e), '\n')

        return df_db


class SQLiteTblPandasDF:
    """
    Conecta con base de datos SQLite y transfiere los datos de la tabla
    indicada a un pandas DataFrame.
    """

    def __init__(self, ruta_db, v):
        self.ruta_db = ruta_db
        self.v = v
        
        self.lista_tablas = []  # Lista con las tablas de la base de datos.
        self.tabla = ''  # Tabla de la base de datos.

    def sql_to_df(self):
        self.importa_sqlite()  # Importa la base de datos.
        self.tablas_sqlite()  # Obtiene las tablas de la base de datos.
        self.tabla_sqlite()  # Selecciona la tabla de la base de datos.
        self.sqlite_df()  # Convierte la tabla de la base dedatos a un DataFrame.

        return self.df

    def importa_sqlite(self):
        self.conn = sqlite3.connect(self.ruta_db)

    def tablas_sqlite(self):
        db_tablas = self.conn.execute(
            'SELECT name FROM sqlite_master WHERE type="table";'
            )
        
        for tabla in db_tablas:
            self.lista_tablas.append(tabla[0])
        
        return self.lista_tablas

    def tabla_sqlite(self):
        input_dialog = InputDialogGetItem(
            self.v,
            'Tablas de la base de datos',
            'Tabla:                                                    \
                ',
            self.lista_tablas)
        self.tabla = input_dialog.get_item()
        
        return self.tabla

    def sqlite_df(self):
        select_from = 'SELECT * FROM ' + self.tabla + ';'
        self.df = pd.read_sql_query(select_from, self.conn)
        
        return self.df
