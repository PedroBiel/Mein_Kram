# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:41:45 2018

@author: pc175
"""

import os
import pandas as pd


class CasosCarga:
    """
    Añade los items en la lista de casos de carga según 
    los items de la lista de archivos csv para implantaciones.
    """
    
    def __init__(self, l0, l1, l2, p):
        
        self.lst_arch = l0               # Lista con los archivos csv para implantaciones.
        self.lst_casos_carga = l1        # Lista con los casos de carga en archivos csv.
        self.lst_casos_carga_grupo = l2  # Lista con los casos de carga en grupo.
        self.pfad = p                    # Ruta donde se encuantran los archivos csv.       
        
    def casos_carga(self):
        
        self.lst_casos_carga.clear()
        self.lst_casos_carga_grupo.clear()
#        self.lst_arch = lst_arch

        lst_arch_impl = []

        for index in range(self.lst_arch.count()):

            arch_csv = self.lst_arch.item(index).text()
            lst_arch_impl.append(arch_csv)
        
        os.chdir(self.pfad)
        os.getcwd()
        lst_arch_csv = [x for x in os.listdir(self.pfad) if x in lst_arch_impl]  # Selecciona de los archivos csv del directorio únicamente los que se encuantran en la lista de archivos csv para implantaciones.
        
        try:  # Para evitar que al eliminar todos los casos de carga en grupo aparezca un error porque no hay nada para concatenar.
            
            self.reacciones = pd.concat((pd.read_csv(f, sep=';', decimal=',') for f in lst_arch_csv))  # DataFrame de pandas con los datos de las reacciones.
            
            print(self.reacciones.columns, '\n')
            print(self.reacciones.round(0), '\n')
            print(self.reacciones.drop_duplicates('Nombre').Nombre, '\n')
            
            casos = self.reacciones.drop_duplicates('Nombre').Caso     
            nombres = self.reacciones.drop_duplicates('Nombre').Nombre
        
            for caso, nombre in zip(casos, nombres):

                lst_cas_carg = str(caso) + ' : ' + nombre
                self.lst_casos_carga.addItem(lst_cas_carg)
                print(lst_cas_carg)
            
        except Exception:
            
            self.reacciones = None
            print('reacciones = None')
            
    def df_reacciones(self):
            
        return self.reacciones