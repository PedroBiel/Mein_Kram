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
from datos.qfiledialog import FileDialog
from datos.sqlite import SQLite

from modelos.treemodel import TreeModel


class CntAbreSqlite:
    """
    """

    def __init__(self, ventana):

        self.v = ventana

        self.nombre_db = ''

    def abre_sqlite(self):
        self.nombre_db = self.ruta_nombre_sqlite()
        self.sqlite_db()
        self.vista_modelo()

    def ruta_nombre_sqlite(self):
        subtitulo = Constantes.OPENFILENAME[0]
        directorio = Constantes.OPENFILENAME[1]
        filtro = Constantes.OPENFILENAME[2]
        fichero = FileDialog(subtitulo, directorio, filtro)
        self.ruta_nombre = fichero.get_open_file_name()

        self.v.log.clear()
        self.v.log.append('Base de datos')
        self.v.log.append('-------------')
        self.v.log.append(self.ruta_nombre)

        return self.ruta_nombre

    def sqlite_db(self):
        sqlite = SQLite(self.nombre_db)
        self.nombre_sqlite = sqlite.nombre_db()
        self.tablas_sqlite = sqlite.tablas_db()
        self.diccionario_sqlite = sqlite.diccionario_db()

        self.v.log.append('')
        self.v.log.append('Nombre')
        self.v.log.append('------')
        self.v.log.append(self.nombre_sqlite)
        self.v.log.append('')
        self.v.log.append('Tablas')
        self.v.log.append('------')
        self.v.log.append(str(self.tablas_sqlite))
        self.v.log.append('')
        self.v.log.append('Diccionario')
        self.v.log.append('-----------')
        self.v.log.append(str(self.diccionario_sqlite))

    def vista_modelo(self):
        model = QStandardItemModel()
        self.v.tre_sqlite.setModel(model)

        tree = TreeModel()
        tree.rellenar_recursivo(
                self.diccionario_sqlite, model.invisibleRootItem()
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
        self.v.view.show()


    def tree_item(self):

        for item in self.v.tre_sqlite.selectedIndexes():
            item_clicked = item.data(Qt.DisplayRole) # or ix.data()
            print(item_clicked)
            
            self.v.log.append('')
            self.v.log.append('Tabla')
            self.v.log.append('-----')
            self.v.log.append(item_clicked)


