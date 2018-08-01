# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:22:12 2018

@author: pc175
"""

from PyQt4 import QtGui

from qtdesigner.dlg_propiedades import *

from clases.datos import Datos


class DialogPropiedades(QtGui.QDialog):
    """Define las propiedades del cuadro de implantación."""
    
    def __init__(self, parent=None):
        
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.cbx_cuadro = self.ui.comboBox_cuadro
        self.cbx_idioma = self.ui.comboBox_idioma
        self.cbx_redondeo = self.ui.comboBox_redondeo
        self.cbx_filas_columnas = self.ui.comboBox_filas_columnas
        
        self.btn_aceptar = self.ui.pushButton_aceptar
        self.btn_cancelar = self.ui.pushButton_cancelar
        
        self.datos_propiedades = Datos()
        
        lst_cuadro = ['Cintas', 'Máquinas']
        lst_idioma = ['Español', 'Inglés', 'Francés']
        lst_redondeo = ['1', '5', '10']
        lst_filas_columnas = ['Puntos/Grupos', 'Grupos/Puntos']
        
        self.cbx_cuadro.addItems(lst_cuadro)
        self.cbx_idioma.addItems(lst_idioma)
        self.cbx_redondeo.addItems(lst_redondeo)
        self.cbx_filas_columnas.addItems(lst_filas_columnas)
        
        self.btn_aceptar.clicked.connect(self.aceptar)
        self.btn_cancelar.clicked.connect(self.cancelar)
        
    def aceptar(self):
        
        self.datos_propiedades.var1 = self.cbx_cuadro.currentText()
        self.datos_propiedades.var2 = self.cbx_idioma.currentText()
        self.datos_propiedades.var3 = self.cbx_redondeo.currentText()
        self.datos_propiedades.var4 = self.cbx_filas_columnas.currentText()
        
        self.close()
        
    def cancelar(self):
        
        self.close()