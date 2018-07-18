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

from PyQt4 import QtCore, QtGui

from classes.EN_1998.part_1._3_ground_conditions_and_seismic_action._3_2_seismic_action_0_0_171106 import SeismicAction

from qtdesigner.main_window_0_0 import *

from clases.estadowidgets import EstadoWidgets


class Window(QtGui.QMainWindow):  # QMainWindow instead of QDialog in order to have minimize button.

    def __init__(self, parent=None):

        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.datos_menu()
        self.datos_entrada()
        self.datos_salida()
        self.estado_inicial()

        # Datos iniciales. Rango del periodo (PROVISIONAL).
        self.T = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])

        # Activar checkbox.
        self.chkbx_EjeX.clicked.connect(self.activar)
        self.chkbx_EjeY.clicked.connect(self.activar)
        self.chkbx_EjeZ.clicked.connect(self.activar)

        # Ejecutar.
        #self.actn_ag_T.triggered.connect(self.aceleracion_periodos)
        self.btn_ag_T.clicked.connect(self.parametros)

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
        self.tbl_parametros = self.ui.tableWidget_Parametros

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

    def parametros(self):

        rows = 0
        cols = 8
        self.direccion = []

        try:

            if self.chkbx_EjeX.isChecked() is True:

                rows += 1
                self.direccion.append('Eje x')

                accion_sismica_x = self.accion_sismica(self.chkbx_EjeX, self.agRx, self.gammaI, self.tipo_terreno,
                                                       self.tipo_espectro, self.T, self.mi, self.q, self.beta)

                agx = accion_sismica_x.design_ground_acceleration()
                S = accion_sismica_x.soil_factor()
                TB = accion_sismica_x.lower_limit_of_the_period()
                TC = accion_sismica_x.upper_limit_of_the_period()
                TD = accion_sismica_x.beginnig_of_the_constant_displacement()
                SeT = accion_sismica_x.horizontal_elastic_response_spectrum()

        except Exception as e:

            self.exception()
            print('Excepción:', e)

        try:

            if self.chkbx_EjeY.isChecked() is True:

                rows += 1
                self.direccion.append('Eje y')

                accion_sismica_y = self.accion_sismica(self.chkbx_EjeY, self.agRy, self.gammaI, self.tipo_terreno,
                                                       self.tipo_espectro, self.T, self.mi, self.q, self.beta)

                agy = accion_sismica_y.design_ground_acceleration()
                S = accion_sismica_y.soil_factor()
                TB = accion_sismica_y.lower_limit_of_the_period()
                TC = accion_sismica_y.upper_limit_of_the_period()
                TD = accion_sismica_y.beginnig_of_the_constant_displacement()
                SeT = accion_sismica_y.horizontal_elastic_response_spectrum()

        except Exception as e:

            self.exception()
            print('Excepción:', e)

        try:

            if self.chkbx_EjeZ.isChecked() is True:

                rows += 1
                self.direccion.append('Eje z')

                accion_sismica_z = self.accion_sismica(self.chkbx_EjeZ, self.agRz, self.gammaI, self.tipo_terreno,
                                                       self.tipo_espectro, self.T, self.mi, self.q, self.beta)

                avgz = accion_sismica_z.vertical_design_ground_acceleration()
                S = accion_sismica_z.soil_factor()
                TBv = accion_sismica_z.vertical_lower_limit_of_the_period()
                TCv = accion_sismica_z.vertical_upper_limit_of_the_period()
                TDv = accion_sismica_z.vertical_beginnig_of_the_constant_displacement()
                SveT = accion_sismica_z.vertical_elastic_response_spectrum()

        except Exception as e:

            self.exception()
            print('Excepción:', e)

        # Rellena tabla.
        self.tbl_parametros.setRowCount(rows)
        self.tbl_parametros.setColumnCount(cols)

        for c in range(cols):

            for r in range(rows):

                if c == 0:  # Columna de dirección.

                    self.valor = str(self.direccion[r])
                    self.rellena_tabla(r, c)

                if c == 1:  # Columna de tipo de espectro.

                    self.valor = self.tipo_espectro.currentText()
                    self.rellena_tabla(r, c)

                if c == 2:  # Columna de tipo de terreno.

                    self.valor = self.tipo_terreno.currentText()
                    self.rellena_tabla(r, c)

                if c == 3:  # Columna de coeficiente de suelo.

                    # if self.direccion[r] == 'Eje x':
                    #
                    #     self.valor = str(agx)
                    #     self.rellena_tabla(r, c)
                    #
                    # elif self.direccion[r] == 'Eje y':
                    #
                    #     self.valor = str(agy)
                    #     self.rellena_tabla(r, c)
                    #
                    # else:
                    #
                    #     self.valor = str(avgz)
                    #     self.rellena_tabla(r, c)

                    self.rellena_columna(r, c, agx, agy, avgz)

                if c == 4:  # Columna del parámetro del suelo.

                    self.valor = str(S)
                    self.rellena_tabla(r, c)

                if c == 5:  # Columna del límite inferior del periodo.

                    if self.direccion[r] == 'Eje x' or self.direccion[r] == 'Eje y':

                        self.valor = str(TB)
                        self.rellena_tabla(r, c)

                    else:

                        self.valor = str(TBv)
                        self.rellena_tabla(r, c)

    def accion_sismica(self, chkbx_eje, agR, gI, ground_type, type_of_spectra, T, m, q, b):


        if chkbx_eje.isChecked() is True:

            agR = float(agR.text())
            gI = float(gI.text())
            ground_type = ground_type.currentText()
            type_of_spectra = type_of_spectra.currentText()
            m = float(m.text())
            q = float(q.text())
            b = float(b.text())

            accion_sismica = SeismicAction(agR, gI, ground_type, type_of_spectra, T, m, q, b)

            return accion_sismica

    def exception(self):

        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.setWindowTitle('¡Aviso!')
        msg.setText('Faltan datos por introducir.')
        msg.exec_()

    def rellena_columna(self, r, c, valor_x, valor_y, valor_z):

        if self.direccion[r] == 'Eje x':

            self.valor = str(valor_x)
            self.rellena_tabla(r, c)

        elif self.direccion[r] == 'Eje y':

            self.valor = str(valor_y)
            self.rellena_tabla(r, c)

        else:

            self.valor = str(valor_z)
            self.rellena_tabla(r, c)

    def rellena_tabla(self, r, c):

        item = QtGui.QTableWidgetItem(self.valor)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tbl_parametros.setItem(r, c, QtGui.QTableWidgetItem(item))

        # Set table width.
        width = self.tbl_parametros.verticalHeader().width()
        width += self.tbl_parametros.horizontalHeader().length()
        if self.tbl_parametros.verticalScrollBar().isVisible():
            width += self.tbl_parametros.verticalScrollBar().width()
        width += self.tbl_parametros.frameWidth() * 2
        self.tbl_parametros.setFixedWidth(width)

        # Set table height.
        header_height = self.tbl_parametros.horizontalHeader().height()
        row_height = self.tbl_parametros.rowHeight(r)
        table_height = self.tbl_parametros.setRowHeight(r, row_height)
        self.tbl_parametros.setFixedHeight(header_height + row_height * (r + 1) + 10)






















    # def objetos_SeismicAction(self):
    #
    #     accion_sismica_x = SeismicAction(self.agRx, self.gammaI, self.tipo_terreno, self.tipo_espectro, self.T, self.mi,
    #                                      self.q, self.beta)
    #     accion_sismica_y = SeismicAction(self.agRy, self.gammaI, self.tipo_terreno, self.tipo_espectro, self.T, self.mi,
    #                                      self.q, self.beta)
    #     accion_sismica_z = SeismicAction(self.agRz, self.gammaI, self.tipo_terreno, self.tipo_espectro, self.T, self.mi,
    #                                      self.q, self.beta)
    #
    #     self.agx = accion_sismica_x.design_ground_acceleration()
    #     self.agy = accion_sismica_y.design_ground_acceleration()
    #     self.avgz = accion_sismica_z.design_ground_acceleration()
    #
    #     self.S = accion_sismica_x.soil_factor()
    #     self.TB = accion_sismica_x.lower_limit_of_the_period()
    #     self.TC = accion_sismica_x.upper_limit_of_the_period()
    #     self.TD = accion_sismica_x.beginnig_of_the_constant_displacement()
    #
    #     self.TBv = accion_sismica_z.vertical_lower_limit_of_the_period()
    #     self.TCv = accion_sismica_z.vertical_upper_limit_of_the_period()
    #     self.TDv = accion_sismica_z.vertical_beginnig_of_the_constant_displacement()
    #
    #     self.SeT = accion_sismica_x.horizontal_elastic_respose_spectrum()
    #     self.SveT = accion_sismica_z.vertical_elastic_respose_spectrum()













    #     # Aceleración y periodos.
    # # -----------------------
    #
    # def aceleracion_periodos(self):
    #
    #     self.aceleracion()
    #     self.periodos()
    #
    # # Aceleración.
    #
    # def accion_sismica(self, chkbx_eje, agR, gI, ground_type, type_of_spectra, T, m, q, b):
    #
    #     if chkbx_eje.isChecked() is True:
    #
    #         agR = float(agR.text())
    #         gI = float(gI.text())
    #         m = float(m.text())
    #         q = float(q.text())
    #         b = float(b.text())
    #
    #         self.accion_sismica = SeismicAction(agR, gI, ground_type, type_of_spectra, T, m, q, b)
    #
    #         return self.accion_sismica
    #
    # def aceleracion(self):
    #
    #     self.agx.clear()
    #     self.agy.clear()
    #     self.avgz.clear()
    #
    #     # Eje X.
    #     try:
    #
    #         if self.chkbx_EjeX.isChecked() is True and self.gammaI != 0 and self.mi != 0 \
    #                                                and self.q != 0 and self.beta != 0:
    #
    #             sismox = self.accion_sismica(self.chkbx_EjeX, self.agRx, self.gammaI, self.tipo_terreno,
    #                                          self.tipo_espectro, self.T, self.mi, self.q, self.beta)
    #             aceleracion_gx = sismox.design_ground_acceleration()
    #             self.agx.setText(str(aceleracion_gx))
    #
    #     except Exception:
    #
    #         self.exception()
    #
    #     # Eje Y.
    #     try:
    #
    #         if self.chkbx_EjeY.isChecked() is True and self.gammaI != 0 and self.mi != 0 and self.q != 0 \
    #                                                and self.beta != 0:
    #
    #             sismoy = self.accion_sismica(self.chkbx_EjeY, self.agRy, self.gammaI, self.tipo_terreno,
    #                                          self.tipo_espectro, self.T, self.mi, self.q, self.beta)
    #             aceleracion_gy = sismoy.design_ground_acceleration()
    #             self.agy.setText(str(aceleracion_gy))
    #
    #     except Exception:
    #
    #         self.exception()
    #
    #     # Eje Z.
    #     try:
    #
    #         if self.chkbx_EjeZ.isChecked() is True and self.gammaI != 0 and self.mi != 0 and self.q != 0 \
    #                                                and self.beta != 0:
    #
    #             sismoz = self.accion_sismica(self.chkbx_EjeZ, self.agRz, self.gammaI, self.tipo_terreno,
    #                                          self.tipo_espectro, self.T, self.mi, self.q, self.beta)
    #             aceleracion_vgz = sismoz.design_ground_acceleration()
    #             self.avgz.setText(str(aceleracion_vgz))
    #
    #     except Exception:
    #
    #         self.exception()
    #
    # def exception(self):
    #
    #     msg = QtGui.QMessageBox()
    #     msg.setIcon(QtGui.QMessageBox.Warning)
    #     msg.setWindowTitle('¡Aviso!')
    #     msg.setText('Faltan datos por introducir.')
    #     msg.exec_()
    #
    # # Periodos.
    #
    # # def periodos(self):
    # #
    # #     print('hola')
    # #
    # #     cols = self.tbl_parametros.columnCount()
    # #     rows = self.tbl_parametros.rowCount()
    # #
    # #     for r in range(rows):
    # #
    # #         for c in range(cols):
    # #
    # #             valor = str(r)+'-'+str(c)
    # #             item = QtGui.QTableWidgetItem(valor)
    # #             item.setTextAlignment(QtCore.Qt.AlignCenter)
    # #             self.tbl_parametros.setItem(r, c, QtGui.QTableWidgetItem(item))
    #
    # def parametros(self):
    #
    #     rows = 0
    #     cols = 6
    #     self.direccion = []
    #
    #     # agRx = float(self.agRx.text())
    #     # agRy = float(self.agRy.text())
    #     # agRz = float(self.agRz.text())
    #     # gammaI = float(self.gammaI.text())
    #     # tipo_terreno = self.tipo_terreno.text()
    #     # tipo_espectro = self.tipo_espectro.text()
    #     # T = self.T
    #     # mi = float(self.mi.text())
    #     # q = float(self.q.text())
    #     # beta = float(self.beta.text())
    #
    #
    #     # # Instanciar objetos de la clase SeismicAction.
    #     # self.sismo_x = SeismicAction(agRx, gammaI, tipo_terreno, tipo_espectro,
    #     #                              T, mi, q, beta)
    #     # self.sismo_y = SeismicAction(agRy, gammaI, tipo_terreno, tipo_espectro,
    #     #                              T, mi, q, beta)
    #     # self.sismo_z = SeismicAction(agRz, gammaI, tipo_terreno, tipo_espectro,
    #     #                              T, mi, q, beta)
    #     #
    #     # self.agx = self.sismo_x.design_ground_acceleration().text()
    #     # self.agy = self.sismo_y.design_ground_acceleration().text()
    #     # self.avgz = self.sismo_z.design_ground_acceleration().text()
    #     # self.S = self.sismo_x.soil_factor()
    #     # self.TB = self.sismo_x.lower_limit_of_the_period()
    #     # self.TC = self.sismo_x.upper_limit_of_the_period()
    #     # self.TD = self.sismo_x.beginnig_of_the_constant_displacement()
    #     # self.SeT = None  # Por ahora
    #
    #     # Eje x.
    #     try:
    #
    #         if self.chkbx_EjeX.isChecked() is True and self.gammaI != 0 and self.mi != 0 and self.q != 0 \
    #                 and self.beta != 0:
    #
    #             rows += 1
    #             #cols += 1
    #
    #             self.direccion.append('Eje x')
    #
    #             accion_sismica_x = self.accion_sismica(self.chkbx_EjeX, self.agRx, self.gammaI, self.tipo_terreno,
    #                                                    self.tipo_espectro, self.T, self.mi, self.q, self.beta)
    #
    #             agx = accion_sismica_x.design_ground_acceleration()
    #             S = accion_sismica_x.soil_factor()
    #             TB = accion_sismica_x.lower_limit_of_the_period()
    #             TC = accion_sismica_x.upper_limit_of_the_period()
    #             TD = accion_sismica_x.beginnig_of_the_constant_displacement()
    #             SeT = accion_sismica_x.horizontal_elastic_respose_spectrum()
    #
    #
    #
    #     except Exception:
    #
    #         self.exception()
    #
    #     # Eje Y.
    #     try:
    #
    #         if self.chkbx_EjeY.isChecked() is True and self.gammaI != 0 and self.mi != 0 and self.q != 0 \
    #                 and self.beta != 0:
    #
    #             rows += 1
    #             #cols += 1
    #
    #             self.direccion.append('Eje y')
    #
    #             sismoy = self.accion_sismica(self.chkbx_EjeY, self.agRy, self.gammaI, self.tipo_terreno,
    #                                          self.tipo_espectro, self.T, self.mi, self.q, self.beta)
    #
    #             aceleracion_gy = sismoy.design_ground_acceleration()
    #
    #
    #
    #     except Exception:
    #
    #         self.exception()
    #
    #     # Eje Z.
    #     try:
    #
    #         if self.chkbx_EjeZ.isChecked() is True and self.gammaI != 0 and self.mi != 0 and self.q != 0 \
    #                 and self.beta != 0:
    #
    #             rows += 1
    #             #cols += 1
    #
    #             self.direccion.append('Eje z')
    #
    #             sismoz = self.accion_sismica(self.chkbx_EjeZ, self.agRz, self.gammaI, self.tipo_terreno,
    #                                          self.tipo_espectro, self.T, self.mi, self.q, self.beta)
    #             aceleracion_vgz = sismoz.design_ground_acceleration()
    #
    #
    #
    #     except Exception:
    #
    #         self.exception()
    #
    #     self.tbl_parametros.setColumnCount(cols)
    #     self.tbl_parametros.setRowCount(rows)
    #
    #     # Rellena tabla.
    #     for c in range(cols):
    #
    #         for r in range(rows):
    #
    #             if c == 0:  # Columna de dirección.
    #
    #                 self.valor = str(self.direccion[r])
    #                 self.rellena_tabla(r, c)
    #
    #             if c == 1:  # Columna de tipo de espectro.
    #
    #                 self.valor = self.tipo_espectro.currentText()
    #                 self.rellena_tabla(r, c)
    #
    #             if c == 2:  # Columna de tipo de terreno.
    #
    #                 self.valor = self.tipo_terreno.currentText()
    #                 self.rellena_tabla(r, c)
    #
    #             if c == 3:  # Columna de coeficiente de suelo.
    #
    #                 self.valor = 'aaa' #self.agx
    #                 self.rellena_tabla(r, c)
    #
    #
    #     print(rows, cols, self.direccion)
    #
    # def rellena_tabla(self, r, c):
    #
    #     item = QtGui.QTableWidgetItem(self.valor)
    #     item.setTextAlignment(QtCore.Qt.AlignCenter)
    #     self.tbl_parametros.setItem(r, c, QtGui.QTableWidgetItem(item))
    #
    #     # Set table width.
    #     width = self.tbl_parametros.verticalHeader().width()
    #     width += self.tbl_parametros.horizontalHeader().length()
    #     if self.tbl_parametros.verticalScrollBar().isVisible():
    #         width += self.tbl_parametros.verticalScrollBar().width()
    #     width += self.tbl_parametros.frameWidth() * 2
    #     self.tbl_parametros.setFixedWidth(width)
    #
    #     # Set table height.
    #     header_height = self.tbl_parametros.horizontalHeader().height()
    #     row_height = self.tbl_parametros.rowHeight(r)
    #     table_height = self.tbl_parametros.setRowHeight(r, row_height)
    #     self.tbl_parametros.setFixedHeight(header_height + row_height * (r + 1) + 10)
    #
    #
    #     print('gI:', self.gammaI.text())
    #     print('tt:', self.tipo_terreno.currentText())
    #     print('te:', self.tipo_espectro.currentText())
    #     print('m:', self.mi.text())
    #     print('q:', self.q.text())
    #     print('b:', self.beta.text())
    #     print('width:', width)
    #     print('header height:', header_height)
    #     print('row height:', row_height)
    #     print('table height:', table_height)
    #     print('nº rows', r + 1)



























if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    myapp = Window()
    myapp.show()
    sys.exit(app.exec_())