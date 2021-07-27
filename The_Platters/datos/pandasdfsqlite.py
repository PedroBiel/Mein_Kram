# -*- coding: utf-8 -*-
"""
Transfiere datos de pandas DataFrame a SQLite

Created on Fri Dec 20 09:11:29 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd
import sqlite3


class PandasDFSQLite:
    """Transfiere los datos a un pandas DataFrame."""

    def __init__(self, ruta_nombre, df, tabla):
        self.ruta_nombre = ruta_nombre  # Ruta y nombre de la base de datos a guardar.
        self.df = df  # DataFrame a convertir.
        self.tabla = tabla  # # Nombre de la tabla de la base de datos.

    def df_to_sql(self):
        conn = sqlite3.connect(self.ruta_nombre)
        self.df.to_sql(
                self.tabla,
                conn,
                if_exists='replace',
                index=False
                )
