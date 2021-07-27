# -*- coding: utf-8 -*-
"""
THE PLATTERS, el generador de placas base TW
Controlador Materiales de pernos

Created on Mon Dec  2 14:16:21 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd

from PyQt5.QtCore import Qt

from datos.constantes import Constantes
from datos.dfmaterialespernos import MaterialPernoDF
from datos.os import Os
from datos.qfiledialog import FileDialog
from datos.sqlitepandasdf import SQLitePandasDF
from datos.sqlites import SQLites


class CntMaterialPerno:
    """
    Controlador del los materiales de los pernos.
    """

    def __init__(self, ventana):
        self.v = ventana

    # Abre SQLite.
    # ------------
    def abre_sqlite(self):
        """Abre bases de datos."""

        self.ruta_db()
        self.sqlite_db()
        self.v.tree_model_materiales_perno()

    def ruta_db(self):
        """Ruta de las bases de datos."""

        subtitulo = Constantes.EXISTING_DIRECTORY[0]
        directorio = Constantes.EXISTING_DIRECTORY[1]
        pfad = FileDialog(subtitulo, directorio)
        self.v.ruta_materiales_perno = pfad.get_existing_directory()

        return self.v.ruta_materiales_perno

    def sqlite_db(self):
        """
        Diccionario con nombres de base de datos, sus tablas y los valores de
        las tablas.
        """

        db = Os(self.v.ruta_materiales_perno, '.db')
        self.lista_db_ext = db.list_dir_ext()
        self.v.lista_db_materiales_perno = db.list_dir_ext_oculta()
        self.columna = 'Calidad'
        sqlites = SQLites(
                self.v.ruta_materiales_perno,
                self.lista_db_ext,
                self.columna,
                )
        self.v.dcc_sqlite = sqlites.diccionario_db_tbl_val()

    # Obtén datos.
    # ------------
    def obten_datos(self):
        self.tree_item()
        self.sqlite_df()
        self.df_datos_material_perno()
        self.df_concat()
        self.v.table_model_materiales_perno()

    def tree_item(self):
        """Item de la vista seleccionada."""

        for item in self.v.treeview_material_perno.selectedIndexes():
            grandparent_clicked = item.parent().parent().data(Qt.DisplayRole)
            parent_clicked = item.parent().data(Qt.DisplayRole)
            child_clicked = item.data(Qt.DisplayRole)

            self.v.db_materiales_perno = grandparent_clicked
            self.v.tabla_materiales_perno = parent_clicked
            self.v.material_perno = child_clicked

    def sqlite_df(self):
        """Pasa datos de SQLite a pandas DataFrame."""

        print(
                self.v.ruta_materiales_perno, '|',
                self.v.db_materiales_perno, '|',
                self.v.tabla_materiales_perno, '|',
                self.v.material_perno
                )
        sqlite_df = SQLitePandasDF(
                self.v.ruta_materiales_perno,
                self.v.db_materiales_perno,
                self.v.tabla_materiales_perno
                )
        self.df_mat = sqlite_df.conecta()

        return self.df_mat

    def df_datos_material_perno(self):
        """DataFrame con los datos del material."""

        material_perno_df = MaterialPernoDF(
                self.v.d,
                self.df_mat,
                self.v.material_perno
                )
        self.v.df_material_perno = material_perno_df.dataframe_material_perno()

        return self.v.df_material_perno

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
