# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:22:52 2018

@author: pc175
"""

class PueblaDialogoRSA:
    
    def __init__(self, reacciones):
        
        self.reacciones = reacciones  # DataFrame de pandas con las reacciones.

        self.reacciones_ = self.reacciones.round(0)
        
    def reacciones_rsa(self):
        
        self.reacciones_ = self.reacciones_.groupby([
            'Modelo', 'Nudo', 'Caso', 'Nombre'])[[
            'Fx', 'Fy', 'Fz', 'Mx', 'My', 'Mz']].sum()
            
        return self.reacciones_

          
class PueblaDialogoImpl:
    
    def __init__(self, reacciones, grupos, dcc_grupos, dcc_apoyos):
        
        self.reacciones = reacciones  # DataFrame de pandas con las reacciones.
        self.grupos = grupos  # Diccionario de grupos.
        self.dcc_grupos = dcc_grupos  # Diccionario-objeto para pasar datos por referencia.
        self.dcc_apoyos = dcc_apoyos  # Diccionario-objeto para pasar datos por referencia.
        
        self.reacciones_ = self.reacciones.round(0)
        
        self.grupo, self.relacion, self.apoyo = [], [], []

    def reacciones_impl(self):
                     
        for row in self.reacciones_.Caso:
            
            for key in self.grupos.keys():
                
                if str(row) in self.dcc_grupos[key]:
                    
                    self.grupo.append(key)
                    self.relacion.append(self.dcc_grupos[key][0])
                    
        self.reacciones_['Grupo'] = self.grupo
        self.reacciones_['Relación'] = self.relacion
        
        for row in self.reacciones_.Nudo:
            
            for key in self.dcc_apoyos.keys():
                
                if str(row) in self.dcc_apoyos[key]:
                    
                    self.apoyo.append(key)
                    
        self.reacciones_['Apoyo'] = self.apoyo
        
        reacciones_max_min = self.reacciones_.groupby([
            'Modelo', 'Apoyo', 'Grupo']).\
            agg({x: [max, min] for x in ['Fx', 'Fy', 'Fz', 'Mx', 'My', 'Mz']})
        
        return reacciones_max_min
        