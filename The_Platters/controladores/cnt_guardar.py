# -*- coding: utf-8 -*-
"""
THE PLATTERS, el generador de placas base TW
Controlador Guaardar

Created on Fri Dec 20 07:48:12 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""

import pandas as pd

from PyQt5.QtWidgets import QInputDialog, QLineEdit

from datos.constantes import Constantes
from datos.pandasdfsqlite import PandasDFSQLite
from datos.pandasdfxlsx import PandasDFXLSX
from datos.qfiledialog import FileDialog


class CntGuarda:
    """Guarda los datos de una placa base."""

    def __init__(self, ventana):
        self.v = ventana
        
    # Guarda SQLite.
    # --------------

    def sqlite(self):
        """Guarda los datos en una base de datos SQLite."""

        self.nombre_tabla()
        self.ruta_db()
        self.df_sqlite()

    def nombre_tabla(self):
        """Nombre de la tabla de la base de datos SQLite."""
        
        self.v.tabla_db, ok = QInputDialog.getText(
            self.v, 'Placa base', 'Nombre de la tabla:', QLineEdit.Normal, ''
            )
        
        if ok and self.v.tabla_db:
            self.v.tabla_db = self.v.tabla_db.replace(' ', '_')  # No puede haber espacios en el nombre de la tabla.
            
            return self.v.tabla_db

    def ruta_db(self):
        """Ruta de la base de datos."""

        subtitulo = Constantes.GUARDAR_PROYECTO
        pfad = FileDialog(subtitulo, '', 'Tipo de ficheros (*.db *.xlsx)')
        self.v.ruta_db = pfad.get_save_file_name()

        return self.v.ruta_db

    def df_sqlite(self):
        """Base de datos SQLite con los datos del DataFrame."""

        df_sql = PandasDFSQLite(self.v.ruta_db, self.v.df, self.v.tabla_db)
        df_sql.df_to_sql()

    # Guarda Excel.
    # -------------

    def excel(self):
        """Guarda los datos en una hoja Excel."""

        self.ruta_xlsx()
        self.df_xlsx()

    def ruta_xlsx(self):
        """Ruta de la hoja Excel."""

        self.v.ruta_xlsx = self.v.ruta_db[:-3] + '.xlsx'

        return self.v.ruta_xlsx

    def df_xlsx(self):
        """Hoja Excel con los datos del DataFrame."""

        df_xlsx = PandasDFXLSX(self.v.ruta_xlsx, self.v.df, self.v.tabla_db)
        df_xlsx.df_to_excel()
