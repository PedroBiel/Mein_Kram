# -*- coding: utf-8 -*-
"""
THE PLATTERS, el generador de placas base TW

Created on Nov 27 7:41 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd
import qdarkstyle
import sys

from PyQt5 import uic
from PyQt5.QtCore import QLibraryInfo, QLocale, QStringListModel, QTranslator
from PyQt5.QtGui import QFont, QIcon, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QHeaderView, QMainWindow, QTreeView

from controladores.cnt_perfil import CntPerfil
from controladores.cnt_npernos import CntNPernos
from controladores.cnt_dpernos import CntDPernos
from controladores.cnt_dimensiones import CntDimensiones
from controladores.cnt_materialperfil import CntMaterialPerfil
from controladores.cnt_materialperno import CntMaterialPerno
from controladores.cnt_materialplaca import CntMaterialPlaca
from controladores.cnt_materialhormigon import CntMaterialHormigon
from controladores.cnt_abrir import CntAbre
from controladores.cnt_guardar import CntGuarda

from modelos.tablemodel import PandasModel
from modelos.treemodel import TreeModel


class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        uic.loadUi('vistas/theplatters.ui', self)

        self.setWindowIcon(QIcon("iconos/python.png"))

        # Objetos de la aplicación.
        # =========================
        self.As = ''  # Área de tensión del perno de anclaje.
        self.b = ''  # Ancho del perfil.
        self.bp = ''  # Ancho de la placa base.
        self.d = ''  # Diámetro del perno.
        self.d_pernos = ''  # Diámetro de los pernos para QTreeView.
        self.d0 = ''  # Diámetro del agujero para el perno,
        self.db_materiales = ''  # Base de datos del material.
        self.db_materiales_hormigon = ''  # Base de datos del material.
        self.db_materiales_perno = ''  # Base de datos del material.
        self.db_materiales_placa = ''  # Base de datos del material.
        self.db_perfiles = ''  # Base de datos del perfil.
        self.dcc_sqlite = {}  # Diccionario con los datos para el QTreeModel.
        self.df = pd.DataFrame  # Pandas DataFrame con los datos.
        self.df_dimensiones = pd.DataFrame  # Pandas DataFrame con las dimensiones de la placa base.
        self.df_dpernos = pd.DataFrame  # Pandas DataFrame con los datos del diámetro de los pernos.
        self.df_npernos = pd.DataFrame  # Pandas DataFrame con los datos del nº de pernos.
        self.df_material = pd.DataFrame  # Pandas DataFrame con los datos del material.
        self.df_material_hormigon = pd.DataFrame  # Pandas DataFrame con los datos del material de los pernos.
        self.df_material_perno = pd.DataFrame  # Pandas DataFrame con los datos del material de los pernos.
        self.df_material_placa = pd.DataFrame  # Pandas DataFrame con los datos del material de los pernos.
        self.df_perfil = pd.DataFrame  # Pandas DataFrame con los datos del perfil.
        self.df_perfiles = pd.DataFrame  # Pandas DataFrame con los datos de los perfiles.
        self.df_vacia = pd.DataFrame  # Pandas DataFrame vacía.
        self.e = ''  # Separación entre el centro del taladro y el borde adyacente.
        self.h = ''  # Canto del perfil.
        self.hp = ''  # Canto de la placa base.
        self.lista_db_materiales = ''  # Lista de las bases de datos de los materiales.
        self.lista_db_perfiles = ''  # Lista de las bases de datos de los perfiles.
        self.lista_df = []  # Lista con los DataFrames para mostrar en el QTableView.
        self.m = ''  # Distancia del eje del taladro a la superficie paralela.
        self.material = ''  # Material.
        self.material_hormigon = ''  # Material.
        self.material_perno = ''  # Material.
        self.material_placa = ''  # Material.
        self.mn = ''  # Espesor del mortero de nivelación.
        self.n_pernos = ''  # Nº de pernos.
        self.p = ''  # Separación entre taladros
        self.perfil = ''  # Perfil.
        self.ruta_db = ''  # Ruta de la base de datos SQLite con los resultados.
        self.ruta_materiales = ''  # Ruta de las bases de datos de los materiales.
        self.ruta_materiales_hormigon = ''  # Ruta de las bases de datos de los materiales.
        self.ruta_materiales_perno = ''  # Ruta de las bases de datos de los materiales.
        self.ruta_materiales_placa = ''  # Ruta de las bases de datos de los materiales.
        self.ruta_perfiles = ''  # Ruta de las bases de datos de los perfiles.
        self.ruta_xlsx = ''  # Ruta de la hoja Excel con los resultados.
        self.tabla_db = ''  # Nombre de la tabla de la base de datos SQLite.
        self.tabla_materiales = ''  # Nombre de la tabla donde se obtienen los valores para el diccionario.
        self.tabla_materiales_hormigon = ''  # Nombre de la tabla donde se obtienen los valores para el diccionario.
        self.tabla_materiales_perno = ''  # Nombre de la tabla donde se obtienen los valores para el diccionario.
        self.tabla_materiales_placa = ''  # Nombre de la tabla donde se obtienen los valores para el diccionario.
        self.tabla_perfiles = ''  # Nombre de la tabla donde se obtienen los valores para el diccionario.
        self.tp = ''  # Espesor de la placa base.
        self.tf = ''  # Espesor del ala del perfil.
        self.tw = ''  # Espesor del alma del perfil.
        self.w = ''  # Separación entre taladros.

        # Instancias de clases.
        # =====================
        self.cnt_perfil = CntPerfil(self)
        self.cnt_n_pernos = CntNPernos(self)
        self.cnt_d_pernos = CntDPernos(self)
        self.cnt_dimensiones = CntDimensiones(self)
        self.cnt_material_perfil = CntMaterialPerfil(self)
        self.cnt_material_perno = CntMaterialPerno(self)
        self.cnt_material_placa = CntMaterialPlaca(self)
        self.cnt_material_hormigon = CntMaterialHormigon(self)
        self.cnt_abre = CntAbre(self)
        self.cnt_guarda = CntGuarda(self)

        # Objetos PyQt.
        # =============
        self.btn_perfil = self.pushButtonPerfil
        self.cbx_n_pernos = self.comboBoxNPernos
        self.cbx_d_pernos = self.comboBoxDPernos
        self.btn_dimensiones = self.pushButtonDimensiones
        # self.btn_material_perfil = self.pushButtonMaterialPerfil
        # self.btn_material_perno = self.pushButtonMaterialPerno
        # self.btn_material_placa = self.pushButtonMaterialPlacaBase
        # self.btn_material_hormigon = self.pushButtonMaterialHormigon
        # self.btn_resistencias = self.pushButtonResistencias
        self.btn_abrir_proyecto = self.pushButtonAbrirProyecto
        self.btn_guardar_proyecto = self.pushButtonGuardarProyecto
        self.tableview = self.tableView
        self.log = self.textEdit

        self.treeview_perfil = QTreeView()
        self.treeview_material_perfil = QTreeView()
        self.treeview_material_perno = QTreeView()
        self.treeview_material_placa = QTreeView()
        self.treeview_material_hormigon = QTreeView()

        # Fuentes.
        # ========
        fuente_btn = QFont()
        fuente_btn.setFamily('Consolas')
        fuente_btn.setPointSize(11)

        fuente_model = QFont()
        fuente_model.setFamily('Consolas')
        fuente_model.setPointSize(10)

        fuente_log = QFont()
        fuente_log.setFamily('Consolas')
        fuente_log.setPointSize(8)

        self.btn_perfil.setFont(fuente_btn)
        # self.btn_material_perfil.setFont(fuente_btn)
        self.cbx_n_pernos.setFont(fuente_btn)
        self.cbx_d_pernos.setFont(fuente_btn)
        # self.btn_material_perno.setFont(fuente_btn)
        # self.btn_material_placa.setFont(fuente_btn)
        # self.btn_material_hormigon.setFont(fuente_btn)
        self.btn_dimensiones.setFont(fuente_btn)

        self.treeview_perfil.setFont(fuente_model)
        # self.treeview_material_perfil.setFont(fuente_model)
        # self.treeview_material_perno.setFont(fuente_model)
        # self.treeview_material_placa.setFont(fuente_model)
        self.treeview_material_hormigon.setFont(fuente_model)

        self.tableview.setFont(fuente_model)
        self.log.setCurrentFont(fuente_log)

        # Añade items a QComboBox.
        # ========================
        n_pernos = self.cnt_n_pernos
        lista_n_pernos = n_pernos.lista_numero_pernos()
        model = QStringListModel(lista_n_pernos)
        self.cbx_n_pernos.setModel(model)
#        self.n_pernos = n_pernos.numero_pernos_inicial()

        pernos = self.cnt_d_pernos
        lista_d = pernos.lista_diametro_pernos()
        model = QStringListModel(lista_d)
        self.cbx_d_pernos.setModel(model)
        self.d_pernos = pernos.diametro_pernos_inicial()

        # DataFrames vacias con la misma dimensión para actualizar QTableView.
        # ====================================================================
        self.df_vacia = pd.DataFrame(
                {'Símbolo': [],
                 'Magnitud': [],
                 'Unidades': [],
                 'Definición': [],
                 'Norma/Estándar': []
                 })
        self.df_perfil = self.df_vacia
        self.df_material = self.df_vacia
        self.df_npernos = self.df_vacia
        self.df_dpernos = self.df_vacia
        self.df_material_perno = self.df_vacia
        self.df_material_hormigon = self.df_vacia
        self.df_material_placa = self.df_vacia
        self.df_dimensiones = self.df_vacia

        self.lista_df = [
                self.df_perfil,
                self.df_material,
                self.df_npernos,
                self.df_dpernos,
                self.df_material_perno,
                self.df_material_placa,
                self.df_material_hormigon,
                self.df_dimensiones
                ]

        # Eventos.
        # ========
        self.btn_perfil.clicked.connect(self.cnt_perfil.abre_sqlite)
        self.treeview_perfil.clicked.connect(self.cnt_perfil.obten_datos)

        # self.btn_material_perfil.clicked.connect(
        #         self.cnt_material_perfil.abre_sqlite
        #         )
        # self.treeview_material_perfil.clicked.connect(
        #         self.cnt_material_perfil.obten_datos
        #         )

        self.cbx_n_pernos.highlighted.connect(
                self.cnt_n_pernos.numero_pernos
                )
        self.cbx_n_pernos.currentIndexChanged.connect(
                self.cnt_n_pernos.numero_pernos
                )

        self.cbx_d_pernos.highlighted.connect(
                self.cnt_d_pernos.diametro_pernos
                )
        self.cbx_d_pernos.currentIndexChanged.connect(
                self.cnt_d_pernos.diametro_pernos
                )

        self.btn_dimensiones.clicked.connect(self.cnt_dimensiones.placa_base)

        # self.btn_material_perno.clicked.connect(
        #         self.cnt_material_perno.abre_sqlite
        #         )
        # self.treeview_material_perno.clicked.connect(
        #         self.cnt_material_perno.obten_datos
        #         )

        # self.btn_material_placa.clicked.connect(
        #         self.cnt_material_placa.abre_sqlite
        #         )
        # self.treeview_material_placa.clicked.connect(
        #         self.cnt_material_placa.obten_datos
        #         )

        # self.btn_material_hormigon.clicked.connect(
        #         self.cnt_material_hormigon.abre_sqlite
        #         )
        # self.treeview_material_hormigon.clicked.connect(
        #         self.cnt_material_hormigon.obten_datos
        #         )

        self.btn_abrir_proyecto.clicked.connect(self.cnt_abre.sqlite)

        self.btn_guardar_proyecto.clicked.connect(self.cnt_guarda.sqlite)
        self.btn_guardar_proyecto.clicked.connect(self.cnt_guarda.excel)

    # Salidas Perfil.
    # ===============
    def tree_model_perfiles(self):
        """Árbol de las bases de datos de perfiles."""

        model = QStandardItemModel()

        tree = TreeModel()
        tree.rellenar_recursivo(
                self.dcc_sqlite, model.invisibleRootItem()
                )

        self.treeview_perfil.setModel(model)
        self.treeview_perfil.setHeaderHidden(True)
        self.treeview_perfil.setWindowTitle('Perfiles')
        self.treeview_perfil.show()

    def table_model_perfiles(self):
        """Tabla con los datos del perfil."""

        self.table_model()
        self.log_perfil()

    # Salidas Materiales.
    # ===================
    def tree_model_materiales(self):
        """Árbol de las bases de datos de materiales."""

        model = QStandardItemModel()

        tree = TreeModel()
        tree.rellenar_recursivo(
                self.dcc_sqlite, model.invisibleRootItem()
                )

        self.treeview_material_perfil.setModel(model)
        self.treeview_material_perfil.setHeaderHidden(True)
        self.treeview_material_perfil.setWindowTitle('Materiales del perfil')
        self.treeview_material_perfil.show()

    def table_model_materiales(self):
        """Tabla con los datos de materiales."""

        self.table_model()
        self.log_material()

    # Salidas Nº de pernos.
    # =====================
    def table_model_numero_pernos(self):
        """Tabla con los datos del nº de pernos."""

        self.table_model()
        self.log_n_pernos()

    # Salidas Diámetro de los pernos.
    # ===============================
    def table_model_diametro_pernos(self):
        """Tabla con los datos del diámetro de los pernos."""

        self.table_model()
        self.log_d_pernos()

    # Salidas Materiales de los pernos.
    # =================================
    def tree_model_materiales_perno(self):
        """Árbol de las bases de datos de materiales de los pernos."""

        model = QStandardItemModel()

        tree = TreeModel()
        tree.rellenar_recursivo(
                self.dcc_sqlite, model.invisibleRootItem()
                )

        self.treeview_material_perno.setModel(model)
        self.treeview_material_perno.setHeaderHidden(True)
        self.treeview_material_perno.setWindowTitle('Materiales del perno')
        self.treeview_material_perno.show()

    def table_model_materiales_perno(self):
        """Tabla con los datos de materiales de los pernos."""

        self.table_model()
        self.log_material_perno()

    # Salidas Materiales de la placa base.
    # ====================================
    def tree_model_materiales_placa(self):
        """Árbol de las bases de datos de materiales de la placa base."""

        model = QStandardItemModel()

        tree = TreeModel()
        tree.rellenar_recursivo(
                self.dcc_sqlite, model.invisibleRootItem()
                )

        self.treeview_material_placa.setModel(model)
        self.treeview_material_placa.setHeaderHidden(True)
        self.treeview_material_placa.setWindowTitle('Materiales del perno')
        self.treeview_material_placa.show()

    def table_model_materiales_placa(self):
        """Tabla con los datos de materiales de la placa base."""

        self.table_model()
        self.log_material_placa()

    # Salidas Materiales de la base de hormigón.
    # ==========================================
    def tree_model_materiales_hormigon(self):
        """Árbol de las bases de datos de materiales de la base de hormigón."""

        model = QStandardItemModel()

        tree = TreeModel()
        tree.rellenar_recursivo(
                self.dcc_sqlite, model.invisibleRootItem()
                )

        self.treeview_material_hormigon.setModel(model)
        self.treeview_material_hormigon.setHeaderHidden(True)
        self.treeview_material_hormigon.setWindowTitle(
                'Materiales de la base de hormigón'
                )
        self.treeview_material_hormigon.show()

    def table_model_materiales_hormigon(self):
        """Tabla con los datos de materiales de la base de hormigón."""

        self.table_model()
        self.log_material_hormigon()

    # Salidas Dimensiones de la placa base.
    # =====================================
    def table_model_dimensiones(self):
        """Tabla con los datos de las dimensiones de la placa base."""

        self.table_model()

    # Salidas Abrir proyecto.
    # =======================
    def table_model_abrir_proyecto(self):
        """Tabla con los datos del proyecto abierto."""
        
        self.table_model()


    # Table Model.
    # ============
    def table_model(self):
        """Tabla con los datos."""

        model = PandasModel(self.df)
        self.tableview.setModel(model)

        header = self.tableview.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)

    # Imprime log.
    # ============
    def log_perfil(self):
        self.log.clear()
        self.log.append('Log')
        self.log.append('===')
        self.log.append('')
        self.log.append('Ruta de las bases de datos de los perfiles')
        self.log.append('------------------------------------------')
        self.log.append(self.ruta_perfiles)

        self.log.append('')
        self.log.append('Bases de datos de los perfiles')
        self.log.append('------------------------------')
        self.log.append(str(self.lista_db_perfiles))
        self.log.append('')

        self.log.append('')
        self.log.append('Base de datos del perfil')
        self.log.append('------------------------')
        self.log.append(self.db_perfiles)
        self.log.append('')
        self.log.append('Tabla del perfil')
        self.log.append('----------------')
        self.log.append(self.tabla_perfiles)
        self.log.append('')
        self.log.append('Perfil')
        self.log.append('-----')
        self.log.append(self.perfil)

        self.log.append('')
        self.log.append(
                'Datos del perfil transferiodos a la tabla de resultados.'
                )

    def log_material(self):
        self.log.append('')
        self.log.append('Ruta de las bases de datos')
        self.log.append('--------------------------')
        self.log.append(self.ruta_materiales)

        self.log.append('')
        self.log.append('Bases de datos de los materiales')
        self.log.append('--------------------------------')
        self.log.append(str(self.lista_db_materiales))

        self.log.append('')
        self.log.append('Base de datos del material')
        self.log.append('--------------------------')
        self.log.append(self.db_materiales)
        self.log.append('')
        self.log.append('Tabla del material')
        self.log.append('------------------')
        self.log.append(self.tabla_materiales)
        self.log.append('')
        self.log.append('Material')
        self.log.append('--------')
        self.log.append(self.material)

        self.log.append('')
        self.log.append(
                'Datos del material transferiodos a la tabla de resultados.'
                )

    def log_n_pernos(self):
        self.log.append('')
        self.log.append('Nº de pernos')
        self.log.append('------------')
        self.log.append(self.n_pernos)

    def log_d_pernos(self):
        self.log.append('')
        self.log.append('Diámetro de los pernos')
        self.log.append('----------------------')
        self.log.append(str(self.d))

    def log_material_perno(self):
        self.log.append('')
        self.log.append('Ruta de las bases de datos')
        self.log.append('--------------------------')
        self.log.append(self.ruta_materiales_perno)

        self.log.append('')
        self.log.append('Bases de datos de los materiales del perno')
        self.log.append('------------------------------------------')
        self.log.append(str(self.lista_db_materiales_perno))

        self.log.append('')
        self.log.append('Base de datos del material del perno')
        self.log.append('------------------------------------')
        self.log.append(self.db_materiales_perno)
        self.log.append('')
        self.log.append('Tabla del material del perno')
        self.log.append('----------------------------')
        self.log.append(self.tabla_materiales_perno)
        self.log.append('')
        self.log.append('Material del perno')
        self.log.append('------------------')
        self.log.append(self.material_perno)

        self.log.append('')
        self.log.append(
                'Datos del material transferiodos a la tabla de resultados.'
                )

    def log_material_placa(self):
        self.log.append('')
        self.log.append('Ruta de las bases de datos')
        self.log.append('--------------------------')
        self.log.append(self.ruta_materiales_placa)

        self.log.append('')
        self.log.append('Bases de datos de los materiales de la placa base')
        self.log.append('-------------------------------------------------')
        self.log.append(str(self.lista_db_materiales_placa))

        self.log.append('')
        self.log.append('Base de datos del material de la placa base')
        self.log.append('-------------------------------------------')
        self.log.append(self.db_materiales_placa)
        self.log.append('')
        self.log.append('Tabla del material de la placa base')
        self.log.append('-----------------------------------')
        self.log.append(self.tabla_materiales_placa)
        self.log.append('')
        self.log.append('Material de la placa base')
        self.log.append('-------------------------')
        self.log.append(self.material_placa)

        self.log.append('')
        self.log.append(
                'Datos del material transferiodos a la tabla de resultados.'
                )

    def log_material_hormigon(self):
        self.log.append('')
        self.log.append('Ruta de las bases de datos')
        self.log.append('--------------------------')
        self.log.append(self.ruta_materiales_hormigon)

        self.log.append('')
        self.log.append(
                'Bases de datos de los materiales de la base de hormigón'
                )
        self.log.append(
                '-------------------------------------------------------'
                )
        self.log.append(str(self.lista_db_materiales_hormigon))

        self.log.append('')
        self.log.append('Base de datos del material del hormigón')
        self.log.append('---------------------------------------')
        self.log.append(self.db_materiales_hormigon)
        self.log.append('')
        self.log.append('Tabla del material del hormigón')
        self.log.append('-------------------------------')
        self.log.append(self.tabla_materiales_hormigon)
        self.log.append('')
        self.log.append('Material del hormigón')
        self.log.append('---------------------')
        self.log.append(self.material_hormigon)

        self.log.append('')
        self.log.append(
                'Datos del material transferiodos a la tabla de resultados.'
                )


if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Traducir el idiona del sistema operativo y texto predeterminado de PyQt.
    qt_translator = QTranslator()
    qt_translator.load(
        'qtbase_' + QLocale.system().name(),
        QLibraryInfo.location(QLibraryInfo.TranslationsPath)
        )
    app.installTranslator(qt_translator)

    # Dark style.
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
