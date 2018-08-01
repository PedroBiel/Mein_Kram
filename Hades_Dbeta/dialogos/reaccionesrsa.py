# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 13:47:46 2018

@author: pc175
"""

from PyQt4 import QtGui

from qtdesigner.dlg_reacciones import *

from clases.datos import Datos


class DialogReaccionesRSA(QtGui.QDialog):
    """Muestra el diálogo con las reacciones RSA."""

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.cbx = self.ui.comboBox
        self.txt_reacciones = self.ui.textEdit
        
        self.datos_reacciones_rsa = Datos()  # Los objetos entre formularios (con sus datos) se pasan por referencia.

        lst_reacciones = [
            'Reacciones RSA por modelo', 'Reacciones RSA por nudo', 
            'Reacciones RSA por caso', 'Reacciones RSA por nombre'
            ]
        self.cbx.addItems(lst_reacciones)        
        
        self.agrupacion_modelo = ['Modelo', 'Nudo', 'Caso', 'Nombre']
        self.agrupacion_nudo = ['Nudo', 'Modelo', 'Caso', 'Nombre']
        self.agrupacion_caso = ['Caso', 'Modelo', 'Nudo', 'Nombre']
        self.agrupacion_nombre = ['Nombre', 'Modelo', 'Nudo', 'Caso']
        self.fuerzas_momentos = ['Fx', 'Fy', 'Fz', 'Mx', 'My', 'Mz']
        
        self.agrupacion = self.agrupacion_modelo
        
        self.cbx.currentIndexChanged.connect(self.seleccion_reacciones_rsa)

    def seleccion_reacciones_rsa(self):
        """
        Selecciona la agrupación de las reacciones para mostrarlas en el dialogo.
        """
        self.reacciones = self.datos_reacciones_rsa.df  # DataFrame de pandas con las reacciones.
        self.reacciones = self.reacciones.round(0)
 
        seleccion_reaccion = self.cbx.currentText()
            
        if seleccion_reaccion == 'Reacciones RSA por modelo':
            
            self.agrupacion = self.agrupacion_modelo
            self.muestra_reacciones()
            
        elif seleccion_reaccion == 'Reacciones RSA por nudo':
            
            self.agrupacion = self.agrupacion_nudo
            self.muestra_reacciones()
             
        elif seleccion_reaccion == 'Reacciones RSA por caso':
            
            self.agrupacion = self.agrupacion_caso
            self.muestra_reacciones()
            
        elif seleccion_reaccion == 'Reacciones RSA por nombre':
            
            self.agrupacion = self.agrupacion_nombre
            self.muestra_reacciones()
            
    def muestra_reacciones(self):
        """Crea el grupo de reacciones."""
        
        reacciones = self.reacciones.groupby(
            self.agrupacion)[
            self.fuerzas_momentos].sum()
            
        self.txt_reacciones.setText(str(reacciones))
