# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 13:47:46 2018

@author: pc175
"""

from PyQt4 import QtGui

from qtdesigner.dlg_reacciones import *

from clases.datos import Datos


class DialogReaccionesImpl(QtGui.QDialog):
    """Muestra el diálogo con las reacciones para implantación."""

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.cbx = self.ui.comboBox
        self.txt_reacciones = self.ui.textEdit
        
        self.datos_reacciones_impl = Datos()  # Los objetos entre formularios (con sus datos) se pasan por referencia.

        lst_reacciones = [
            'Implantaciones por modelo', 
            'Implantaciones por apoyo', 
            'Implantaciones por grupo'
            ]
        self.cbx.addItems(lst_reacciones)

        self.agrupacion_modelo = ['Modelo', 'Apoyo', 'Grupo']
        self.agrupacion_apoyo = ['Apoyo', 'Modelo', 'Grupo']
        self.agrupacion_grupo = ['Grupo', 'Modelo', 'Apoyo']
        self.fuerzas_momentos = ['Fx', 'Fy', 'Fz', 'Mx', 'My', 'Mz']
        self.cols = ['Fx', 'Fy', 'Fz', 'Mx', 'My', 'Mz']
        
        self.agrupacion = self.agrupacion_modelo
        
        self.cbx.currentIndexChanged.connect(self.seleccion_reacciones_impl)

    def seleccion_reacciones_impl(self):
        """
        Selecciona la agrupación de las reacciones para mostrarlas en el dialogo.
        """
        
        self.reacciones = self.datos_reacciones_impl.df  # DataFrame de pandas con las reacciones.
        self.reacciones = self.reacciones.round(0)
        dicc_grupos = self.datos_reacciones_impl.dcc
        dicc_apoyos = self.datos_reacciones_impl.dcc1
        
        grupo, relacion, apoyo = [], [], []
        
        for row in self.reacciones.Caso:
            
            for key in dicc_grupos.keys():
                
                if str(row) in dicc_grupos[key]:
                    
                    grupo.append(key)
                    relacion.append(dicc_grupos[key][0])
                    
        self.reacciones['Grupo'] = grupo
        self.reacciones['Relación'] = relacion
        
        for row in self.reacciones.Nudo:
            
            for key in dicc_apoyos.keys():
                
                if str(row) in dicc_apoyos[key]:
                    
                    apoyo.append(key)
                    
        self.reacciones['Apoyo'] = apoyo
        
        seleccion_reaccion = self.cbx.currentText()
            
        if seleccion_reaccion == 'Implantaciones por modelo':
            
            self.agrupacion = self.agrupacion_modelo
            self.muestra_reacciones()
            
        elif seleccion_reaccion == 'Implantaciones por apoyo':
            
            self.agrupacion = self.agrupacion_apoyo
            self.muestra_reacciones()
             
        elif seleccion_reaccion == 'Implantaciones por grupo':
            
            self.agrupacion = self.agrupacion_grupo
            self.muestra_reacciones()
            
    def muestra_reacciones(self):
        """Crea el grupo de reacciones."""
        
        reacciones = self.reacciones.groupby(self.agrupacion).\
            agg({x: [max, min] for x in self.fuerzas_momentos})  
                
        self.txt_reacciones.setText(str(reacciones[self.cols]))
