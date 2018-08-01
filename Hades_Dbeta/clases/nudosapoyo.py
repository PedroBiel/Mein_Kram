# -*- coding: utf-8 -*-
"""
Created on Thu May 31 12:44:48 2018

@author: pc175
"""

class NudosApoyo:
    """
    Añade los items en la lista de nudos con apoyo según 
    los items de la lista de archivos csv para implantaciones.
    """
    
    def __init__(self, l0, l1, l2, r):
        
        self.lst_arch = l0                 # Lista con los archivos csv para implantaciones.
        self.lst_nudos_apoyo = l1          # Lista con los nudos con apoyo en archivos csv.
        self.lst_apoyos_implantacion = l2  # Lista con los casos de carga en grupo.  
        self.reacciones = r                # DataFrame de pandas con los datos de las reacciones.
        
    def nudos_apoyo(self):
        
        self.lst_nudos_apoyo.clear()
        self.lst_apoyos_implantacion.clear()
        
        try:  # Para evitar que al trabajar con la DataFrame de las reacciones aparezca un error porque está vacía.
    
            nudos = self.reacciones.drop_duplicates('Nudo').Nudo
        
            for nudo in nudos:
                
                self.lst_nudos_apoyo.addItem(str(nudo))
            
        except Exception:
            
            self.reacciones = None
            print('reacciones = None')
