# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:58:24 2018

@author: pc175
"""

from clases.messagebox import MessageBox

class Apoyos:
    """Crea una lista listWidget de apoyos con los nudos de otra lista listWidget."""
    
    def __init__(self, l1, l2, nd, py, b1, b2, dicc_apoyos):
        
        self.lst_nudos = l1        # Lista con los nudos.
        self.lst_apoyos = l2       # Lista con los apoyos.
        self.nudos = nd            # nombre del nudo.
        self.apoyo = py            # Nombre del apoyo.
        self.btn_nudos = b1        # Botón para seleccionar nudos.
        self.btn_apoyos = b2       # Botón para seleccionar apoyos.
        self.apoyos = dicc_apoyos  # Diccionario con los apoyos.
        
        self.lst_nudos_apoyo = []  # Lista de nudos por apoyo.
        
    def selecciona_nudos(self):
        """Selecciona los nudos de la listWidget lst_nudos."""
        
        str_nudos = ''
        lista_nudos = []
        
        if self.nudos.text() != '':  # Comprueba que no hay ya un nudo seleccionado.
            
            for n in self.nudos.text().split():
                
                self.lst_nudos.addItem(n)
            
            self.nudos.clear()
            
        for item in self.lst_nudos.selectedItems():  # Añade items a lineEdit.
        
            str_nudos = str_nudos + item.text() + ' '
            lista_nudos.append(item.text())
            
            self.nudos.setText(str_nudos)
            
        for SelectedItem in self.lst_nudos.selectedItems():  # Elimina items de lst_1.
            
            self.lst_nudos.takeItem(self.lst_nudos.row(SelectedItem))
            
        self.apoyo.setFocus()
        
    def deselecciona_nudos(self):
        """
        Deselecciona los nudos del QlineEdit lineEdit_nudos y los devuelve a la
        listWidget lst_nudos.
        """
        
        for n in self.nudos.text().split():
                
            self.lst_nudos.addItem(n)
            
        self.nudos.clear()
        
    def crea_apoyo(self):
        """
        self.comprueba_nudos_seleccionados() 
        self.comprueba_nombre_apoyo()
        self.comprueba_apoyo_duplicado()
        self.cr_apoyo()
        """
        
        self.comprueba_nudos_seleccionados()        
    
    def comprueba_nudos_seleccionados(self):
        """Comrpueba que hay nudos seleccionados."""
        
        if self.nudos.text() == '':
            
            msg = MessageBox('Warning', 'Seleccionar al menos un nudo para el apoyo.')
            msg.show_message_box()
            
            self.btn_nudos.setFocus()
            
        else:
            
            self.comprueba_nombre_apoyo()
    
    def comprueba_nombre_apoyo(self):
        """Comprueba que se ha introducido un nombre para el apoyo."""
        
        if self.apoyo.text() == '':
            
            msg = MessageBox('Warning', 'Introducir un nombre para el apoyo.')
            msg.show_message_box()
            
            self.apoyo.setFocus()
            
        else:
            
            self.comprueba_apoyo_duplicado()
            
    def comprueba_apoyo_duplicado(self):
        """Comprueba que el nombre del apoyo no está duplicado."""
        
        try:        
                      
            if self.apoyo.text().upper() in self.apoyos.keys():
                
                msg = MessageBox('Warning', 'El nombre del nuevo apoyo ya existe.')
                msg.show_message_box()
                
                self.apoyo.setFocus()
                
            else:
                
                self.cr_apoyo()
                
        except Exception:
            
            self.apoyos = None
            print('spam')
            
    def cr_apoyo(self):
        """
        Crea los apoyos para implantaciones;
        genera los items en la listWidget lst_apoyos y
        crea el DataFrames con los apoyos y sus correspondientes nudos.
        """
        
        nud = ''
        
        for n in self.nudos.text().split():
            
            self.lst_nudos_apoyo.append(n)
            nud = nud + n + ', '
        
        nv_apoyo = self.apoyo.text().upper()
        
        nuevo_apoyo_ = nv_apoyo + ' : ' + nud[:-2]
        
        self.lst_apoyos.addItem(nuevo_apoyo_)
        self.apoyos[nv_apoyo] = self.lst_nudos_apoyo
        print(self.apoyos)
        
        self.nudos.clear()
        self.apoyo.clear()
        #self.apoyo.setFocus()
        self.btn_nudos.setFocus()
        
    def dicc_apoyos(self):
        
        return self.apoyos
        