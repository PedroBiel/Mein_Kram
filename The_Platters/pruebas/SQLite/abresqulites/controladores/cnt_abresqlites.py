# -*- coding: utf-8 -*-
"""
DESCRIPCIÓN

Created on Fri Nov 15 14:05:49 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItemModel

from datos.constantes import Constantes
from datos.os import Os
from datos.qfiledialog import FileDialog
from datos.sqlites import SQLites

from modelos.treemodel import TreeModel


class CntAbreSqlites:
    """
    """

    def __init__(self, ventana):

        self.v = ventana

        self.nombre_db = ''

    def abre_sqlite(self):
        self.ruta_db = self.ruta_db()
        self.sqlite_db()
        self.vista_modelo()

    def ruta_db(self):
        subtitulo = Constantes.EXISTING_DIRECTORY[0]
        directorio = Constantes.EXISTING_DIRECTORY[1]
        pfad = FileDialog(subtitulo, directorio, 'xx')
        self.ruta = pfad.get_existing_directory()

        self.v.log.clear()
        self.v.log.append('Ruta de las bases de datos')
        self.v.log.append('--------------------------')
        self.v.log.append(self.ruta)

    def sqlite_db(self):
        db = Os(self.ruta, '.db')
        self.lista_db_ext = db.list_dir_ext()
        self.lista_db = db.list_dir_ext_oculta()
        sqlites = SQLites(self.ruta, self.lista_db_ext)
        self.dcc_sqlite = sqlites.diccionario_db()

        self.v.log.append('')
        self.v.log.append('Bases de datos')
        self.v.log.append('--------------')
        self.v.log.append(str(self.lista_db))
        self.v.log.append('')
        self.v.log.append('Diccionario')
        self.v.log.append('-----------')
        self.v.log.append(str(self.dcc_sqlite))

    def vista_modelo(self):
        model = QStandardItemModel()
        self.v.tre_sqlite.setModel(model)

        tree = TreeModel()
        tree.rellenar_recursivo(
                self.dcc_sqlite, model.invisibleRootItem()
                )

        self._proxyModel = QSortFilterProxyModel()
        self._proxyModel.setSourceModel(model)
        self._proxyModel.setDynamicSortFilter(True)
        self._proxyModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.v.tre_sqlite.setModel(self._proxyModel)
        self.v.filtro.textChanged.connect(self._proxyModel.setFilterRegExp)
        self.v.tre_sqlite.setSortingEnabled(True)

        self.v.view.setModel(model)
        self.v.view.setHeaderHidden(True)
        self.v.view.setWindowTitle('Bases de datos')
        self.v.view.show()

    def tree_item(self):

        for item in self.v.tre_sqlite.selectedIndexes():
            item_clicked = item.data(Qt.DisplayRole)  # or ix.data()
            print(item_clicked)

            self.v.log.append('')
            self.v.log.append('Tabla')
            self.v.log.append('-----')
            self.v.log.append(item_clicked)
