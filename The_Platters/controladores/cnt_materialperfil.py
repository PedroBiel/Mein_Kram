# -*- coding: utf-8 -*-
"""
THE PLATTERS, el generador de placas base TW
Controlador Materiales

Created on Fri Nov 29 11:15:11 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd

from PyQt5.QtCore import Qt

from datos.constantes import Constantes
from datos.dfmateriales import MaterialDF
from datos.os import Os
from datos.qfiledialog import FileDialog
from datos.sqlitepandasdf import SQLitePandasDF
from datos.sqlites import SQLites


class CntMaterialPerfil:
    """
    Controlador del los materiales de los perfiles.
    """

    def __init__(self, ventana):
        self.v = ventana

    # Abre SQLite.
    # ------------
    def abre_sqlite(self):
        """Abre bases de datos."""

        self.ruta_db()
        self.sqlite_db()
        self.v.tree_model_materiales()

    def ruta_db(self):
        """Ruta de las bases de datos."""

        subtitulo = Constantes.EXISTING_DIRECTORY[0]
        directorio = Constantes.EXISTING_DIRECTORY[1]
        pfad = FileDialog(subtitulo, directorio)
        self.v.ruta_materiales = pfad.get_existing_directory()

        return self.v.ruta_materiales

    def sqlite_db(self):
        """
        Diccionario con nombres de base de datos, sus tablas y los valores de
        las tablas.
        """

        db = Os(self.v.ruta_materiales, '.db')
        self.lista_db_ext = db.list_dir_ext()
        self.v.lista_db_materiales = db.list_dir_ext_oculta()
        self.columna = 'Calidad'
        sqlites = SQLites(
                self.v.ruta_materiales,
                self.lista_db_ext,
                self.columna,
                )
        self.v.dcc_sqlite = sqlites.diccionario_db_tbl_val()

    # Obtén datos.
    # ------------
    def obten_datos(self):
        self.tree_item()
        self.sqlite_df()
        self.df_datos_material()
        self.df_concat()
        self.v.table_model_materiales()

    def tree_item(self):
        """Item de la vista seleccionada."""

        for item in self.v.treeview_material_perfil.selectedIndexes():
            grandparent_clicked = item.parent().parent().data(Qt.DisplayRole)
            parent_clicked = item.parent().data(Qt.DisplayRole)
            child_clicked = item.data(Qt.DisplayRole)

            self.v.db_materiales = grandparent_clicked
            self.v.tabla_materiales = parent_clicked
            self.v.material = child_clicked

    def sqlite_df(self):
        """Pasa datos de SQLite a pandas DataFrame."""

        print(
                self.v.ruta_materiales, '|',
                self.v.db_materiales, '|',
                self.v.tabla_materiales, '|',
                self.v.material
                )
        sqlite_df = SQLitePandasDF(
                self.v.ruta_materiales,
                self.v.db_materiales,
                self.v.tabla_materiales
                )
        self.df_mat = sqlite_df.conecta()

        return self.df_mat

    def df_datos_material(self):
        """DataFrame con los datos del material."""

        material_df = MaterialDF(
                self.v.df_perfil,
                self.df_mat,
                self.v.material
                )
        self.v.df_material = material_df.dataframe_material()

        return self.v.df_material

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
