# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 08:18:55 2018

@author: pc175
"""

from clases.messagebox import MessageBox
from clases.pasaitems import PasaItems


class GruposImplantacion:
    """
    Añade los items en la lista de grupos para cuadro de implantación según las 
    claves del diccionario de grupos.
    """
    
    def __init__(self, dcc, l1, l2, cbx, dcc_coeficientes):
        
        self.dcc = dcc  # Diccionario de grupos.
        self.lst_1 = l1  # Lista con los grupos para implantación.
        self.lst_2 = l2  # Lista con los coeficientes para implantación.
        self.cbx = cbx  # ComboBox con los coeficientes de implantación.
        self.coeficientes_impl = dcc_coeficientes  # Diccionario con los coeficientes de implantación.
        self.lst_orden_grp = []  # Lista con el orden de los grupos.

#        self.cbx.setCurrentIndex(4)

        self.lst_2.itemPressed.connect(self.orden_grupos)
        
    def grupos_implantacion(self):
        """Añade los grupos de implantación a lst_1."""
        
        self.lst_1.clear()
        
        for key in self.dcc.keys():
            
            self.lst_1.addItem(key)
            
        self.lst_1.sortItems()
        
    def aplica_coeficiente(self):
        """
        Caso especial cuando la lista 1 contiene los coeficientes para el 
        cuadro de implantación con el formato:
        
        coeficiente ' * ' nombre_de_grupo
        
        A la lista 2 se pasan solo los grupos.
        """
        
        if not self.lst_1.selectedItems():  # Comrpueba que hay grupos seleccionados.
            
            msg = MessageBox('Warning', 'Seleccionar al menos un grupo para aplicar el coeficiente de implantación.')
            msg.show_message_box()
            
        else:
        
            coeficiente = self.cbx.currentText()
            
            for item in self.lst_1.selectedItems():  # Añade items a lst_2.
            
                print('item:', item.text(), '; coeficiente: ', coeficiente)
            
                clave_grupo = item.text()
                self.lst_2.addItem(coeficiente + ' * ' + clave_grupo)
                self.coeficientes_impl[clave_grupo] = coeficiente  # Crea diccionario con los grupos y sus coeficientes de implantación.
                
            self.lst_2.sortItems()
            print(self.coeficientes_impl)
            
            for SelectedItem in self.lst_1.selectedItems():  # Elimina items de lst_1.
                
                self.lst_1.takeItem(self.lst_1.row(SelectedItem))
                
            self.sustituye()
            self.orden_grupos()
                
    def aplica_coeficiente_todos(self):
        """
        Caso especial cuando la lista 1 contiene los apoyos con el formato:
        
        coeficiente ' * ' nombre_de_grupo
        
        A la lista 2 se pasan solo los apoyos.
        """
        
        coeficiente = self.cbx.currentText()
        
        for index in range(self.lst_1.count()):  # Añade items a lst_2.

            clave_grupo = self.lst_1.item(index).text()
            self.lst_2.addItem(coeficiente + ' * ' + clave_grupo)
            self.coeficientes_impl[clave_grupo] = coeficiente  # Crea diccionario con los grupos y sus coeficientes de implantación.

            
        self.lst_2.sortItems()  # Ordena items en lst_2.
        self.lst_1.clear()  # Elimina items de lst_1.
        print(self.coeficientes_impl)
        
        self.sustituye()
        self.orden_grupos()
        
    def sustituye(self):
        """
        Sustituye en el diccionario el decimal del coeficiente ',' por '.'.
        """
        
        for key in self.coeficientes_impl.keys():
                
            self.coeficientes_impl[key] = self.coeficientes_impl[key].replace(',', '.')
            
        print(self.coeficientes_impl)
        
    def dicc_coeficientes_impl(self):
        
        return self.coeficientes_impl
        
    def orden_grupos(self):
        
        for index in range(self.lst_2.count()):
            
            item = self.lst_2.item(index).text()
            
            self.lst_orden_grp.append(item)
            
        print(self.lst_orden_grp, '\n')
        
    def orden_grupos_modificado(self, *args):
        
                
        for i in range(self.lst_2.count()):
            
            item = self.lst_2.item(i)
            self.lst_orden_grp.append(item.text())
            
        print(self.lst_orden_grp, '\n')
            
                
            
