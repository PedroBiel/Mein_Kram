# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:30:00 2017

@author: Pedro Biel
@copyright: © 2018, CodEng
@version: 0.0
@email: structural.eng.biel@gmail.com

Poseidon
EN 1998-1:2004
Eurocódigo 8: Proyecto de estructuras sismorresistentes
Parte 1: Reglas generales, acciones sísmicas y reglas para la edificación
Espectro de respuesta elástica y espéctro de cálculo para el análisis elástico
"""


import sys

import numpy as np
import matplotlib.pyplot as plt

from PyQt4 import QtCore, QtGui

from classes.EN_1998.part_1._3_ground_conditions_and_seismic_action._3_2_seismic_action_0_0_171106 import SeismicAction

from qtdesigner.main_window_0_0 import *

from clases.estadowidgets import EstadoWidgets
from clases.formasespectro import FormasEspectro
from clases.messagebox import MessageBox
from clases.parametrossismicos import ParametrosSismicos
from clases.rellenatabla import RellenaTabla, AnchoTabla


class Window(QtGui.QMainWindow):  # QMainWindow instead of QDialog in order to have minimize button.

    def __init__(self, parent=None):

        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.datos_menu()
        self.datos_entrada()
        self.datos_salida()
        self.estado_inicial()
        self.ancho_tabla()

        # Datos iniciales. Rango del periodo (PROVISIONAL).
        self.T = np.arange(0., 4., 0.1)
        self.T = np.append(self.T, 4.)
        print('T:', self.T)

        self.direccion_tipo_terreno_x = []  # Direccion y tipo del espextro, tipo de terreno. List para rellenar tabla.
        self.direccion_tipo_terreno_y = []  # Direccion y tipo del espextro, tipo de terreno. List para rellenar tabla.
        self.direccion_tipo_terreno_z = []  # Direccion y tipo del espextro, tipo de terreno. List para rellenar tabla.

        # Activar checkbox.
        self.chkbx_EjeX.clicked.connect(self.activar)
        self.chkbx_EjeY.clicked.connect(self.activar)
        self.chkbx_EjeZ.clicked.connect(self.activar)

        # Ejecutar.
        #self.actn_ag_T.triggered.connect(self.aceleracion_periodos)
        self.btn_ag_T.clicked.connect(self.parametros)
        self.btn_respuesta_elastica.clicked.connect(self.forma_respuesta_elastica)
        self.btn_analisis_elastico.clicked.connect(self.forma_analisis_elastico)


    def datos_menu(self):

        self.actn_ag_T = self.ui.action_ag_T

    def datos_entrada(self):

        self.chkbx_EjeX = self.ui.checkBox_EjeX
        self.chkbx_EjeY = self.ui.checkBox_EjeY
        self.chkbx_EjeZ = self.ui.checkBox_EjeZ

        self.lbl_agRx = self.ui.label_agRx
        self.lbl_agRy = self.ui.label_agRy
        self.lbl_agRz = self.ui.label_agRz

        self.agRx = self.ui.lineEdit_agRx  # Aceleración máxima de referencia del suelo en un terreno tipo A en la dirección x.
        self.agRy = self.ui.lineEdit_agRy  # Aceleración máxima de referencia del suelo en un terreno tipo A en la dirección y.
        self.agRz = self.ui.lineEdit_agRz  # Aceleración máxima de referencia del suelo en un terreno tipo A en la dirección z.
        self.agRx.setValidator(QtGui.QDoubleValidator())
        self.agRy.setValidator(QtGui.QDoubleValidator())
        self.agRz.setValidator(QtGui.QDoubleValidator())

        self.gammaI = self.ui.lineEdit_GammaI               # Coeficiente de importancia.
        self.tipo_terreno = self.ui.comboBox_TipoTerreno    # Tipo de terreno.
        self.tipo_espectro = self.ui.comboBox_TipoEspectro  # Tipo de espectro.
        self.mi = self.ui.lineEdit_Mi                       # Coeficiente de corrección del amortiguamiento.
        self.q = self.ui.lineEdit_q                         # Coeficiente de comportamiento.
        self.beta = self.ui.lineEdit_Beta                   # Coeficiente correspondiente al umbral inferior del espectro de cálculo horizontal.
        self.gammaI.setValidator(QtGui.QDoubleValidator())
        self.mi.setValidator(QtGui.QDoubleValidator())
        self.q.setValidator(QtGui.QDoubleValidator())
        self.beta.setValidator(QtGui.QDoubleValidator())

    def datos_salida(self):

        self.btn_ag_T = self.ui.pushButton_ag_T
        self.btn_respuesta_elastica = self.ui.pushButton_respuesta_elastica
        self.btn_analisis_elastico = self.ui.pushButton_analisis_elastico
        self.tbl_parametros = self.ui.tableWidget_Parametros

        self.rows = 0  # Número de fila inicial en tabla de parámetros.
        self.cols = 8  # Número de columnas en tabla de parámetros.

    def estado_inicial(self):
        """Color y activación iniciales de los widgets."""

        self.estado_x = EstadoWidgets(self.chkbx_EjeX, self.lbl_agRx, self.agRx)
        self.estado_x.chkbx_activado()
        self.estado_x.lbl_activado()
        self.estado_x.lndt_activado()

        self.estado_y = EstadoWidgets(self.chkbx_EjeY, self.lbl_agRy, self.agRy)
        self.estado_y.chkbx_desactivado()
        self.estado_y.lbl_desactivado()
        self.estado_y.lndt_desactivado()

        self.estado_z = EstadoWidgets(self.chkbx_EjeZ, self.lbl_agRz, self.agRz)
        self.estado_z.chkbx_desactivado()
        self.estado_z.lbl_desactivado()
        self.estado_z.lndt_desactivado()

    def activar(self):
        """Activa los widgets si CheckBox ischecked."""

        self.estado_x.activa_widgets()
        self.estado_y.activa_widgets()
        self.estado_z.activa_widgets()

    def ancho_tabla(self):
        """Ancho inicial de la tabla de parámetros."""

        ancho_tabla = AnchoTabla(self.tbl_parametros)
        ancho_tabla.set_table_width()

    def parametros(self):

        self.rows = 0

        try:

            # Eje X.
            if self.chkbx_EjeX.isChecked():

                direccion = 'Horizontal X'

                parametros_sismicos_x = ParametrosSismicos(
                    self.chkbx_EjeX, direccion, self.agRx, self.gammaI, self.tipo_terreno,
                    self.tipo_espectro, self.T, self.mi, self.q, self.beta
                )
                self.parametros_x = parametros_sismicos_x.parametros_horizontales()
                self.SeTx = parametros_sismicos_x.SeT()
                self.SdTx = parametros_sismicos_x.SdT()


                print(self.parametros_x)
                print(self.SeTx)
                print(self.SdTx)

            # Eje Y.
            if self.chkbx_EjeY.isChecked():

                direccion = 'Horizontal Y'

                parametros_sismicos_y = ParametrosSismicos(
                    self.chkbx_EjeY, direccion, self.agRy, self.gammaI, self.tipo_terreno,
                    self.tipo_espectro, self.T, self.mi, self.q, self.beta
                )
                self.parametros_y = parametros_sismicos_y.parametros_horizontales()
                self.SeTy = parametros_sismicos_y.SeT()
                self.SdTy = parametros_sismicos_y.SdT()

                print(self.parametros_y)
                print(self.SeTy)
                print(self.SdTy)

            # Eje Z.
            if self.chkbx_EjeZ.isChecked():

                direccion = 'Vertical Z'

                parametros_sismicos_z = ParametrosSismicos(
                    self.chkbx_EjeZ, direccion, self.agRz, self.gammaI, self.tipo_terreno,
                    self.tipo_espectro, self.T, self.mi, self.q, self.beta
                )
                self.parametros_z = parametros_sismicos_z.parametros_verticales()
                self.SveTz = parametros_sismicos_z.SeT()
                self.SvdTz = parametros_sismicos_z.SdT()

                print(self.parametros_z)
                print(self.SveTz)
                print(self.SvdTz)

            self.rellena_tabla()

        except Exception as e:

            self.exception()
            print('Excepción:', e)

    def exception(self):

        msg = MessageBox('Warning', 'Faltan datos por introducir.')
        msg.show_message_box()

    def rellena_tabla(self):

        # Eje X.
        if self.chkbx_EjeX.isChecked() is True:

            rellena_tabla_x = RellenaTabla(self.rows, self.tbl_parametros, self.parametros_x)
            rellena_tabla_x.rellena_tabla()
            self.rows = rellena_tabla_x.filas()

        # Eje Y.
        if self.chkbx_EjeY.isChecked() is True:

            rellena_tabla_y = RellenaTabla(self.rows, self.tbl_parametros, self.parametros_y)
            rellena_tabla_y.rellena_tabla()
            self.rows = rellena_tabla_y.filas()

        # Eje Z.
        if self.chkbx_EjeZ.isChecked() is True:

            rellena_tabla_z = RellenaTabla(self.rows, self.tbl_parametros, self.parametros_z)
            rellena_tabla_z.rellena_tabla()
            self.rows = rellena_tabla_z.filas()

        print(self.rows, self.cols)

    def forma_respuesta_elastica(self):

        self.parametros()

        # plt.style.use('seaborn-darkgrid')
        # plt.style.use('dark_background')

        fig, ax = plt.subplots()

        x = self.T
        print('x:', x)
        max_y = 0

        if self.chkbx_EjeZ.isChecked() is True:

            y3 = self.SveTz
            ax.plot(x, y3, color='b', linewidth=2, label='$S_{ve}(T)_z$')

            if max_y < max(y3):

                max_y = max(y3)

        if self.chkbx_EjeY.isChecked() is True:

            y2 = self.SeTy
            ax.plot(x, y2, color='g', linewidth=2, label='$S_e(T)_y$')

            if max_y < max(y2):

                max_y = max(y2)

        if self.chkbx_EjeX.isChecked() is True:

            y1 = self.SeTx
            ax.plot(x, y1, color='r', linewidth=2, label='$S_e(T)_x$')

            if max_y < max(y1):

                max_y = max(y1)

        print('max_y:', max_y)

        ax.axis([0, 4, 0, max_y + 0.5])
        # plt.ylim(max_y + 0.5)
        ax.set_xlabel('$T$ [s]', fontsize=14)
        ax.set_ylabel('$S_e(T)$ [g]', fontsize=14)
        ax.legend(prop={'size': 14})
        ax.set_title('Shapes of the elastic response spectrum', fontsize=16)
        plt.show()

    def forma_analisis_elastico(self):

        FormasEspectro(self.chkbx_EjeX, self.chkbx_EjeY, self.chkbx_EjeZ, self.T, self.SdTx, self.SdTy, self.SvdTz).plt_show()




        # S = [1.0, 2.0, 1.0, 0.66666666666666663, 0.5, 0.32000000000000001, 0.22222222222222224, 0.16326530612244899, 0.125]
        #
        #
        # x = self.T
        # y = S
        # plt.plot(x, y)
        # plt.show()
















if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    myapp = Window()
    myapp.show()
    sys.exit(app.exec_())