# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:30:00 2017

@author: Pedro Biel
@copyright: © 2017, CodEng
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

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.EN_1998.EN_1998_0_0_171106 import EN_1998

from classes.EN_1998.EN_1998_0_0_171106 import *

from qtdesigner.poseidon_0_0 import *


class Window(QtGui.QMainWindow):  # QMainWindow instead of QDialog in order to have minimize button.

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Datos de entrada.

        self.chkbx_EjeX = self.ui.checkBox_EjeX
        self.chkbx_EjeY = self.ui.checkBox_EjeY
        self.chkbx_EjeZ = self.ui.checkBox_EjeZ

        self.lbl_agRx = self.ui.label_agRx
        self.lbl_agRy = self.ui.label_agRy
        self.lbl_agRz = self.ui.label_agRz

        self.agRx = self.ui.lineEdit_agRx  # Aceleración máxima de referencia del suelo en un terreno tipo A en la dirección x.
        self.agRy = self.ui.lineEdit_agRy  # Aceleración máxima de referencia del suelo en un terreno tipo A en la dirección y.
        self.agRz = self.ui.lineEdit_agRz  # Aceleración máxima de referencia del suelo en un terreno tipo A en la dirección z.
        self.agRx.setValidator(QDoubleValidator())
        self.agRy.setValidator(QDoubleValidator())
        self.agRz.setValidator(QDoubleValidator())

        self.gammaI = self.ui.lineEdit_GammaI               # Coeficiente de importancia.
        self.tipo_terreno = self.ui.comboBox_TipoTerreno    # Tipo de terreno.
        self.tipo_espectro = self.ui.comboBox_TipoEspectro  # Tipo de espectro.
        self.mi = self.ui.lineEdit_Mi                       # Coeficiente de corrección del amortiguamiento.
        self.q = self.ui.lineEdit_q                         # Coeficiente de comportamiento.
        self.beta = self.ui.lineEdit_Beta                   # Coeficiente correspondiente al umbral inferior del espectro de cálculo horizontal.
        self.gammaI.setValidator(QDoubleValidator())
        self.q.setValidator(QDoubleValidator())
        self.beta.setValidator(QDoubleValidator())

        # Datos de salida.

        self.lbl_ejeX = self.ui.label_EjeX
        self.lbl_ejeY = self.ui.label_EjeY
        self.lbl_ejeZ = self.ui.label_EjeZ

        self.lbl_agx = self.ui.label_agx
        self.lbl_agy = self.ui.label_agy
        self.lbl_avgz = self.ui.label_avgz

        self.agx = self.ui.lineEdit_agx
        self.agy = self.ui.lineEdit_agy
        self.avgz = self.ui.lineEdit_avgz

        # Color inicial de chekbox.
        self.chkbx_EjeX.setStyleSheet('color: black')  # Activado.
        self.chkbx_EjeY.setStyleSheet('color: gray')   # Desactivado.
        self.chkbx_EjeZ.setStyleSheet('color: gray')   # Desactivado.

        # Color inicial de label a.gR.
        self.lbl_agRx.setStyleSheet('color: black')  # Activado.
        self.lbl_agRy.setStyleSheet('color: gray')   # Desactivado.
        self.lbl_agRz.setStyleSheet('color: gray')   # Desactivado.

        # Activación inicial de lineEdit_agR.
        self.agRx.setEnabled(True)   # Activado.
        self.agRy.setEnabled(False)  # Desactivado.
        self.agRz.setEnabled(False)  # Desactivado.

        # Color inicial de label_Eje.
        self.lbl_ejeX.setStyleSheet('color: black')  # Activado.
        self.lbl_ejeY.setStyleSheet('color: gray')   # Desactivado.
        self.lbl_ejeZ.setStyleSheet('color: gray')   # Desactivado.

        # Color inicial de label_ag.
        self.lbl_agx.setStyleSheet('color: black')  # Activado.
        self.lbl_agy.setStyleSheet('color: gray')   # Desactivado.
        self.lbl_avgz.setStyleSheet('color: gray')  # Desactivado.

        # Activar checkbox.
        QtCore.QObject.connect(self.chkbx_EjeX, QtCore.SIGNAL('clicked()'), self.activar)
        QtCore.QObject.connect(self.chkbx_EjeY, QtCore.SIGNAL('clicked()'), self.activar)
        QtCore.QObject.connect(self.chkbx_EjeZ, QtCore.SIGNAL('clicked()'), self.activar)

        # Aceleración del suelo y periodos
        self.T = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
        QObject.connect(self.ui.pushButton_ag_T, QtCore.SIGNAL('clicked()'), self.aceleracion_periodos)

    # Activa campos.
    # --------------

    def activa_chkbx(self, chkbx_eje, lbl_agR, agR, lbl_eje, lbl_ag, ag):

        if chkbx_eje.isChecked() is True:

            chkbx_eje.setStyleSheet('color: black')
            lbl_agR.setStyleSheet('color: black')
            agR.setEnabled(True)
            lbl_eje.setStyleSheet('color: black')
            lbl_ag.setStyleSheet('color: black')

        else:

            chkbx_eje.setStyleSheet('color: gray')
            lbl_agR.setStyleSheet('color: gray')
            agR.setEnabled(False)
            lbl_eje.setStyleSheet('color: gray')
            lbl_ag.setStyleSheet('color: gray')

    def activar(self):

        # Eje X.
        self.activa_chkbx(self.chkbx_EjeX, self.lbl_agRx, self.agRx, self.lbl_ejeX, self.lbl_agx, self.agx)

        # Eje Y.
        self.activa_chkbx(self.chkbx_EjeY, self.lbl_agRy, self.agRy, self.lbl_ejeY, self.lbl_agy, self.agy)

        # Eje Z.
        self.activa_chkbx(self.chkbx_EjeZ, self.lbl_agRz, self.agRz, self.lbl_ejeZ, self.lbl_avgz, self.avgz)

    # Aceleración y periodos.
    # -----------------------

    def accion_sismica(self, chkbx_eje, agR, gI, ground_type, type_of_spectra, T, m, q, b):

        if chkbx_eje.isChecked() is True:

            agR = float(agR.text())
            gI = float(gI.text())
            m = float(m.text())
            q = float(q.text())
            b = float(b.text())

            accionsismica = EN_1998(agR, gI, ground_type, type_of_spectra, T, m, q, b)
            return accionsismica

    def aceleracion_periodos(self):

        # Eje X.
        sismox = self.accion_sismica(self.chkbx_EjeX, self.agRx, self.gammaI, self.tipo_terreno, self.tipo_espectro,
                                     self.T, self.mi, self.q, self.beta)
        agx = sismox.design_ground_acceleration()
        self.agx.setText(str(agx))

        # Eje Y.
        sismoy = self.accion_sismica(self.chkbx_EjeY, self.agRy, self.gammaI, self.tipo_terreno, self.tipo_espectro,
                                     self.T, self.mi, self.q, self.beta)
        agy = sismoy.design_ground_acceleration()
        self.agy.setText(str(agy))



















if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    myapp = Window()
    myapp.show()
    sys.exit(app.exec_())