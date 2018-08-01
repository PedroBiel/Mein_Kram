# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:58:24 2018

@author: pc175
"""

from clases.messagebox import MessageBox

class Puntos:
    """Crea una lista listWidget de puntos con los apoyos de otra lista listWidget."""
    
    def __init__(self, l1, l2, py, pt, b1, b2, dicc_puntos):
        
        self.lst_apoyos = l1       # Lista con los apoyos.
        self.lst_puntos = l2       # Lista con el número de puntos.
        self.apoyos = py            # nombre del apoyo.
        self.puntos = pt            # Nombre del punto.
        
        self.btn_apoyos = b1        # Botón para seleccionar apoyos.
        self.btn_apoyos = b2       # Botón para seleccionar apoyos.
        self.puntos = dicc_puntos  # Diccionario con los apoyos.
        
        self.lst_puntos_apoyo = []  # Lista de puntos por apoyo.
        
    def selecciona_apoyos(self):
        """Selecciona los apoyos de la listWidget lst_apoyos."""
        
        str_apoyos = ''
        lista_apoyos = []
        
        if self.apoyos.text() != '':  # Comprueba que no hay ya un apoyo seleccionado.
            
            for n in self.apoyos.text().split():
                
                self.lst_apoyos.addItem(n)
            
            self.apoyos.clear()
            
        for item in self.lst_apoyos.selectedItems():  # Añade items a lineEdit.
        
            str_apoyos = str_apoyos + item.text() + ' '
            lista_apoyos.append(item.text())
            
            self.apoyos.setText(str_apoyos)
            
        for SelectedItem in self.lst_apoyos.selectedItems():  # Elimina items de lst_1.
            
            self.lst_apoyos.takeItem(self.lst_apoyos.row(SelectedItem))
            
        self.apoyo.setFocus()
        
    def deselecciona_nudos(self):
        """
        Deselecciona los nudos del QlineEdit lineEdit_nudos y los devuelve a la
        listWidget lst_apoyos.
        """
        
        for n in self.nudos.text().split():
                
            self.lst_apoyos.addItem(n)
            
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
        genera los items en la listWidget lst_puntos y
        crea el DataFrames con los apoyos y sus correspondientes nudos.
        """
        
        nud = ''
        
        for n in self.nudos.text().split():
            
            self.lst_apoyos_apoyo.append(n)
            nud = nud + n + ', '
        
        nv_apoyo = self.apoyo.text().upper()
        
        nuevo_apoyo_ = nv_apoyo + ' : ' + nud[:-2]
        
        self.lst_puntos.addItem(nuevo_apoyo_)
        self.apoyos[nv_apoyo] = self.lst_apoyos_apoyo
        print(self.apoyos)
        
        self.nudos.clear()
        self.apoyo.clear()
        #self.apoyo.setFocus()
        self.btn_nudos.setFocus()
        
    def dicc_apoyos(self):
        
        return self.apoyos
        