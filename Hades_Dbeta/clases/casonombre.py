# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:47:36 2018

@author: pc175
"""

class CasoNombre:
    """
    Sustituye los items numéricos de un listWidget por su caso y nombre
    del DataFrame de pandas self.reacciones.
    """
    
    def __init__(self, lst, df):
        
        self.lst = lst   # Lista donde incluir caso y nombre.
        self.df = df     # DataFrame de pandas donde filtrar los items de la lista.
        self.items = []

    
    def caso_nombre(self):
        
        for index in range(self.lst.count()):  # Añade items a lst.
            
            self.items.append(self.lst.item(index).text())
                   
        nuevo_df = self.df[self.df['Caso'].isin(self.items)]  # Nuevo DataFrame con los items.
        casos = nuevo_df.drop_duplicates('Nombre').Caso
        nombres = nuevo_df.drop_duplicates('Nombre').Nombre

        self.lst.clear()
        
        for caso, nombre in zip(casos, nombres):  # Añade casos y nombres a lst.
            
            lst_cas_carg = str(caso) + ' : ' + nombre
            self.lst.addItem(lst_cas_carg)