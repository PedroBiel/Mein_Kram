# -*- coding: utf-8 -*-
"""
THE PLATTERS, el generador de placas base TW
Controlador Abrir

Created on Wed Jan  8 14:40:54 2020

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


from datos.constantes import Constantes
from datos.sqlitepandasdf import SQLiteTblPandasDF
from datos.qfiledialog import FileDialog


class CntAbre:
    """Abre los datos de una placa base."""
    
    def __init__(self, ventana):
        self.v = ventana

    # Abre SQLite.
    # ------------

    def sqlite(self):
        """Abre los datos en una base de datos SQLite."""

        self.ruta_db()
        self.sqlite_df()
        self.v.table_model_abrir_proyecto()

    def ruta_db(self):
        """Ruta de la base de datos."""

        subtitulo = Constantes.ABRIR_PROYECTO
        pfad = FileDialog(subtitulo, '', 'Tipo de ficheros (*.db)')
        self.v.ruta_db = pfad.get_open_file_name()
        print('ruta_db:', self.v.ruta_db)

        return self.v.ruta_db

    def sqlite_df(self):
        """
        Pasa datos de la base de datos SQLite con los datos a un DataFrame.
        """

        sql_df = SQLiteTblPandasDF(self.v.ruta_db, self.v)
        self.v.df = sql_df.sql_to_df()
        
        print('df:', self.v.df)
