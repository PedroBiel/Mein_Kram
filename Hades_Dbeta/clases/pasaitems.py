# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:45:09 2018

@author: pc175
"""        
        
class PasaItems:
    """Intercambio de items entre listas QListWidget."""
    
    def __init__(self, l1, l2):
        
        self.lst_1 = l1  # Lista 1.
        self.lst_2 = l2  # Lista 2.
        
        self.lst = []    # Lista con los casos.
        self.clv = []    # Lista con las claves del diccionario de grupos para eliminar.
        
    def pasa_items(self):  # Pasa items de la lista lst_1 a la lista lst_2.
        
        for item in self.lst_1.selectedItems():  # Añade items a lst_2.

            self.lst_2.addItem(item.text())

        for SelectedItem in self.lst_1.selectedItems():  # Elimina items de lst_1.
            
            self.lst_1.takeItem(self.lst_1.row(SelectedItem))

        self.lst_2.sortItems()  # Ordena items en lst_2.
    
    def pasa_todos_items(self):  # Pasa todos los items de la lista lst_1 a la lista lst_2.

        for index in range(self.lst_1.count()):  # Añade items a lst_2.

            index = self.lst_1.item(index).text()
            self.lst_2.addItem(index)

        self.lst_2.sortItems()  # Ordena items en lst_2.
        self.lst_1.clear()  # Elimina items de lst_1.
        
    def pasa_items_grupo(self):  # Pasa items de la lista lst_1 a la lista lst_2.
        """
        Caso especial cuando la lista 1 contiene los grupos de casos de carga
        con el formato:
        
        nombre_de_grupo ' : ' caso1 ' +/o ' caso2 ...
        
        A la lista 2 se pasan solo los casos.
        """
              
        for self.item in self.lst_1.selectedItems():  # Crea lista con claves y añade items a lst_2.
                   
            i = 0
                   
            for caracter in self.item.text().split():
                
                if i == 0:  # caracter[0] == clave del diccionario con los grupos de casos de carga.
                
                    self.clv.append(caracter)
                    i += 1
                    
                if caracter.isdigit():  # Añade items a lst_2
                    
                    self.lst.append(int(caracter))
        
        for item in self.lst:
            
            self.lst_2.addItem(str(item))

        for SelectedItem in self.lst_1.selectedItems():  # Elimina items de lst_1.
            
            self.lst_1.takeItem(self.lst_1.row(SelectedItem))
            
    def pasa_todos_items_grupo(self):  # Pasa todos los items de la lista lst_1 a la lista lst_2.
        """
        Caso especial cuando la lista 1 contiene los grupos de casos de carga 
        con el formato:
        
        nombre_de_grupo ' : ' caso1 ' +/o ' caso2 ...
        
        A la lista 2 se pasan solo los casos.
        """
        
        for index in range(self.lst_1.count()):  # Añade items a lst_2.

            index = self.lst_1.item(index).text()
            
            for caracter in index.split():
                    
                if caracter.isdigit():
                    
                    self.lst.append(int(caracter))
                    
        for item in self.lst:
            
            self.lst_2.addItem(str(item))
        
        self.lst_1.clear()  # Elimina items de lst_1.
        
    def pasa_items_apoyo(self):
        """
        Caso especial cuando la lista 1 contiene los apoyos con el formato:
        
        nombre_de_apoyo ' : ' apoyo1 ', ' apoyo2 ...
        
        A la lista 2 se pasan solo los apoyos.
        """
        
        self.pasa_items_grupo()

    def pasa_todos_items_apoyo(self):  # Pasa todos los items de la lista lst_1 a la lista lst_2.
        """
        Caso especial cuando la lista 1 contiene los apoyos con el formato:
        
        nombre_de_apoyo ' : ' apoyo1 ', ' apoyo2 ...
        
        A la lista 2 se pasan solo los apoyos.
        """
        
        self.pasa_todos_items_grupo()
        
    def pasa_items_coeficiente(self):  # Pasa items de la lista lst_1 a la lista lst_2.
        """
        Caso especial cuando la lista 1 contiene los coeficientes para el 
        cuadro de implantación con el formato:
        
        coeficiente ' * ' nombre_de_grupo
        
        A la lista 2 se pasan solo los grupos.
        """
              
        for self.item in self.lst_1.selectedItems():  # Crea lista con claves y añade items a lst_2.
                   
            i = 0
                   
            for caracter in self.item.text().split():
                
                if i == 2:  # caracter[0] == clave del diccionario con los grupos de casos de carga.
                
                    self.clv.append(caracter)
                    self.lst.append(caracter)
                    
                i += 1
        
        for item in self.lst:
            
            self.lst_2.addItem(str(item))

        for SelectedItem in self.lst_1.selectedItems():  # Elimina items de lst_1.
            
            self.lst_1.takeItem(self.lst_1.row(SelectedItem))
            
    def pasa_todos_items_coeficiente(self):  # Pasa todos los items de la lista lst_1 a la lista lst_2.
        """
        Caso especial cuando la lista 1 contiene los apoyos con el formato:
        
        coeficiente ' * ' nombre_de_grupo
        
        A la lista 2 se pasan solo los apoyos.
        """        
        
        for index in range(self.lst_1.count()):  # Añade items a lst_2.
        
            index = self.lst_1.item(index).text()
            
            for caracter in index.split():
                    
                if caracter.isalpha():
                    
                    self.lst.append(str(caracter))
                    
        for item in self.lst:
            
            self.lst_2.addItem(str(item))
        
        self.lst_1.clear()  # Elimina items de lst_1.
        
        
    def claves(self):  # Claves del diccionario para eliminar.
    
        return self.clv
        