# -*- coding: utf-8 -*-
"""
THE PLATTERS, el generador de placas base TW
Controlador Perfil

Created on Tue Nov 26 14:35:29 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd

from PyQt5.QtCore import Qt

from datos.constantes import Constantes
from datos.dfperfiles import PerfilDF
from datos.os import Os
from datos.qfiledialog import FileDialog
from datos.sqlitepandasdf import SQLitePandasDF
from datos.sqlites import SQLites


class CntPerfil:
    """
    Controlador de perfiles.
    """

    def __init__(self, ventana):
        self.v = ventana

    # Abre SQLite.
    # ------------
    def abre_sqlite(self):
        """Abre bases de datos."""

        self.ruta_db()
        self.sqlite_db()
        self.v.tree_model_perfiles()

    def ruta_db(self):
        """Ruta de las bases de datos."""

        subtitulo = Constantes.EXISTING_DIRECTORY[0]
        directorio = Constantes.EXISTING_DIRECTORY[1]
        pfad = FileDialog(subtitulo, directorio)
        self.v.ruta_perfiles = pfad.get_existing_directory()

        return self.v.ruta_perfiles

    def sqlite_db(self):
        """
        Diccionario con nombres de base de datos, sus tablas y los valores de
        las tablas.
        """

        db = Os(self.v.ruta_perfiles, '.db')
        self.lista_db_ext = db.list_dir_ext()
        self.v.lista_db_perfiles = db.list_dir_ext_oculta()
        self.columna = 'nominal'
        sqlites = SQLites(
                self.v.ruta_perfiles,
                self.lista_db_ext,
                self.columna)
        self.v.dcc_sqlite = sqlites.diccionario_db_tbl_val()

    # Obtén datos.
    # ------------
    def obten_datos(self):
        self.tree_item()
        self.sqlite_df()
        self.df_datos_perfil()
        self.df_concat()
        self.v.table_model_perfiles()

    def tree_item(self):
        """Item de la vista seleccionada."""

        for item in self.v.treeview_perfil.selectedIndexes():
            grandparent_clicked = item.parent().parent().data(Qt.DisplayRole)
            parent_clicked = item.parent().data(Qt.DisplayRole)
            child_clicked = item.data(Qt.DisplayRole)

            self.v.db_perfiles = grandparent_clicked
            self.v.tabla_perfiles = parent_clicked
            self.v.perfil = child_clicked

    def sqlite_df(self):
        """Pasa datos de SQLite a pandas DataFrame."""

        print(
                self.v.ruta_perfiles, '|',
                self.v.db_perfiles, '|',
                self.v.tabla_perfiles
                )
        sqlite_df = SQLitePandasDF(
                self.v.ruta_perfiles,
                self.v.db_perfiles,
                self.v.tabla_perfiles
                )
        self.v.df_perfiles = sqlite_df.conecta()

        return self.v.df_perfiles

    def df_datos_perfil(self):
        """DataFrame con los datos del perfil."""

        perfil_df = PerfilDF(self.v.df_perfiles, self.v.perfil)
        self.v.df_perfil = perfil_df.dataframe_perfil()

        return self.v.df_perfil

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
