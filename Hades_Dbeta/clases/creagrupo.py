# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:19:10 2018

@author: pc175
"""

from clases.messagebox import MessageBox

class CreaGrupo:
    
    def __init__(self, lst_ccg, lst_g, nvgrp, dicc_grupos, rbt_Y, rbt_O):
        
        self.lst_casos_carga_grupo = lst_ccg  # Lista de casos de carga en grupo.
        self.lst_grupos = lst_g               # Lista de grupos de casos de carga.
        self.nuevo_grupo = nvgrp              # Nuevo grupo.
        self.grupos = dicc_grupos             # Diccionario con los grupos de casos de carga.
        self.rbt_Y = rbt_Y                    # radioButton de la relación 'Y'.
        self.rbt_O = rbt_O                    # radioButton de la relación 'O'.
        
    
    def crea_grupo(self):
        """
        self.comprueba_casos_seleccionados() 
        self.comprueba_nombre_grupo()
        self.comprueba_grupo_duplicado()
        self.cr_grupo()
        """
        
        self.comprueba_casos_seleccionados() 
        
    def comprueba_casos_seleccionados(self):
        """Comrpueba que hay casos seleccionados."""
        
        if self.lst_casos_carga_grupo.count() == 0:
            
            msg = MessageBox('Warning', 'Seleccionar al menos un caso de carga para el grupo.')
            msg.show_message_box()
            
            self.nuevo_grupo.setFocus()
            
        else:
            
            self.comprueba_nombre_grupo()
            
    def comprueba_nombre_grupo(self):
        """Comprueba que se ha introducido un nombre para el grupo."""
        
        if self.nuevo_grupo.text() == '':
            
            msg = MessageBox('Warning', 'Introducir un nombre para el grupo.')
            msg.show_message_box()
            
            self.nuevo_grupo.setFocus()
            
        else:
            
            self.comprueba_grupo_duplicado()
            
    def comprueba_grupo_duplicado(self):
        """Comprueba que el nombre del grupo no está duplicado."""
        
        try:        
                      
            if self.nuevo_grupo.text().upper() in self.grupos.keys():
                
                msg = MessageBox('Warning', 'El nombre del nuevo grupo ya existe.')
                msg.show_message_box()
                
                self.nuevo_grupo.selectAll()
                self.nuevo_grupo.setFocus()
                
            else:
                
                self.cr_grupo()
                
        except Exception:
            
            self.grupos = None
            print('spam')
            
    def cr_grupo(self):
        """
        Crea los grupos para implantaciones;
        genera los items en la listWidget lst_grupos_casos_carga y
        crea el DataFrames con los grupos y sus correspondientes casos.
        """
    
        self.nv_grp = self.nuevo_grupo.text().replace(' ', '_').upper()  # Sustituye ' ' por '_' para mantener la cadena unida. Em mayusculas.

        if self.rbt_Y.isChecked():    # Si la relación es Y incluye 'Y' en el primer item.
                
            casos = ['Y']
            
        elif self.rbt_O.isChecked():  # Si la relación es O exclusivo incluye 'O' en el primer item.
        
            casos = ['O']
            
        else:                         # Si no la relación es Y/O inclusivo, incluye '¤' en el primer item.
            
            casos = ['¤']

        for index in range(self.lst_casos_carga_grupo.count()):  # Crea lista con los casos por grupo.
            
            caso = self.lst_casos_carga_grupo.item(index).text()
            index = caso.index(' ')
            caso = caso[:index]
            
            casos.append(caso)
        
        self.grupos[self.nv_grp] = casos  # Crea diccionario con los grupos y sus casos.
        print(self.grupos)
        
        cas = ''
        
        for c in casos[1:]:  # Incluye los grupos y sus casos en la lista listWidget.

            if self.rbt_Y.isChecked():
                
                cas = cas + c + ' + '
                
            elif self.rbt_O.isChecked():
                
                cas = cas + c + ' o '
                
            else:

                cas = cas + c + ' ¤ '
            
        nuevo_grupo_ = self.nv_grp + ' : ' + cas[:-3]
           
        self.lst_grupos.addItem(nuevo_grupo_)
        self.nuevo_grupo.setText('')
        self.nuevo_grupo.setFocus()
        self.lst_casos_carga_grupo.clear()
        
    def dicc_grupos(self):
        
        return self.grupos
