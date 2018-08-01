# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 14:26:38 2018

@author: pc175
"""

#import sys
#sys.path.append('C:\Python\Apps\Hades\Hades_D')
#for row in sys.path: print(row)


from PyQt4 import QtGui

from qtdesigner.dlg_proyecto import *

from clases.datos import Datos


class DialogProyecto(QtGui.QDialog):
    """Muestra el dialogo con los datos de proyecto."""
    
    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.proyecto = self.ui.lineEdit_proyecto
#        self.proyecto.selectAll()
        self.elemento = self.ui.lineEdit_elemento
        self.empresa = self.ui.lineEdit_empresa
        self.autor = self.ui.lineEdit_autor
        self.comentarios = self.ui.plainTextEdit_comentarios
        
        self.btn_aceptar = self.ui.pushButton_aceptar
        self.btn_cancelar = self.ui.pushButton_cancelar
        
        self.datos_proyecto = Datos()
          
        self.proyecto.setText(self.datos_proyecto.var1)
#        self.proyecto.selectAll()
        self.elemento.setText(self.datos_proyecto.var2)
        self.empresa.setText(self.datos_proyecto.var3)
        self.autor.setText(self.datos_proyecto.var4)
        self.comentarios.setPlainText(self.datos_proyecto.var5)
        
        self.btn_aceptar.clicked.connect(self.aceptar)
        self.btn_cancelar.clicked.connect(self.cancelar)
        
    def aceptar(self):
        
        self.datos_proyecto.var1 = self.proyecto.text()
        self.datos_proyecto.var2 = self.elemento.text()
        self.datos_proyecto.var3 = self.empresa.text()
        self.datos_proyecto.var4 = self.autor.text()
        self.datos_proyecto.var5 = self.comentarios.toPlainText()
        
        self.close()
        
    def cancelar(self):
        
        self.close()
