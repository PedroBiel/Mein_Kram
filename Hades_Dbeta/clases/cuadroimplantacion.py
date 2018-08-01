# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:48:58 2018

@author: pc175
"""
from PyQt4 import QtGui

import os
import xlsxwriter
import time


class CuadroImplantacion:
    
    def __init__(self, proyecto, elemento, autor, cuadro, idioma, redondeo, filas_columnas, apoyos):
        
        self.proyecto = proyecto
        self.elemento = elemento
        self.autor = autor
        self.cuadro = cuadro
        self.idioma = idioma
        self.redondeo = redondeo
        self.filas_columnas = filas_columnas
        self.apoyos = apoyos
        self.lst_apoyos = []
        print('self.apoyos:', self.apoyos)
        
        self.i, self.j = 7, 1  # Coordenadas de la celda inicial del cuadro de implantación.
    
        self.archivo_xlsx = ''
        
        self.cabecero_tabla_cinta = [
            'CARGAS POR PUNTO [kN]',
            'LOADS PER POINT [kN]',
            'CHARGES PAR POINT [kN]'
            ]
        self.cabecero_tabla_maquina = [
            'CARGAS POR RUEDA / PUNTO DE ANCLAJE [kN]',
            'LOADS PER WHEEL / ANCHORING POINT [kN]',
            'CHARGES PAR ROUE [kN]'
            ]
        self.punto_tabla_cinta = [
            'PUNTO',
            'POINT',
            'POINT'
            ]
        self.punto_tabla_maquina = [
            'RUEDA/PUNTO',
            'WHEEL/POINT',
            'ROUE/POINT'
            ]
        self.n_puntos_tabla_cinta = [
            'Nº DE PUNTOS',
            'POINT NUMBER',
            'NOMBRE DE POINTS'
            ]
        self.n_puntos_tabla_maquina = [
            
            'Nº DE RUEDAS/PUNTOS',
            'No OF WHEELS/POINTS',
            'NOMBRE DE ROUES/POINTS'
            ]
        self.combinaciones_tabla = [
            'COMBINACIONES DE CARGA',
            'LOAD COMBINATIONS',
            'COMBINAISON DE CHARGE'
            ]
        

        
        
    
    def crea_xlsx(self):
        
        self.archivo_xlsx = QtGui.QFileDialog.getSaveFileName(None, 'Save file', '', '*.xlsx;; All Files (*.*)')
        print(self.archivo_xlsx)
        
        self.crea_libro()
        self.pie_pagina()
        self.formato()
        self.titulo()
        self.cuadro_tabla()
        self.filas_columnas_tabla()
        self.filas_tabla()
        
        
        
        
        
        self.cierra_libro()
        

    def crea_libro(self):
        
        self.workbook = xlsxwriter.Workbook(self.archivo_xlsx, {'strings_to_numbers': True})
        self.workbook.set_properties({
            'title': self.proyecto,
            'subject': self.elemento,
            'author': self.autor
            })
            
        self.worksheet = self.workbook.add_worksheet(self.elemento)
            
    def pie_pagina(self):
        
        footer = '&L&6&"Monospac821 BT" &F / {} &R&6&"Monospac821 BT" &P/&N'.format(self.autor)
        self.worksheet.set_footer(footer)
        
    def formato(self):
        
        self.worksheet.hide_gridlines(2)  # Oculta líneas de cuadrícula
        
    def titulo(self):
        
        titulo = 'Implantaciones'
        fecha = time.strftime('%Y.%m.%d')
        
        formato_titulo = self.workbook.add_format()
        formato_titulo.set_bold()
        formato_titulo.set_font_size(18)
        
        self.worksheet.write('A1', titulo, formato_titulo)
        self.worksheet.write('A2', fecha)
        self.worksheet.write('A4', 'Proyecto:')
        self.worksheet.write('A5', 'Elemento:')
        self.worksheet.write('A6', 'Autor:')
        self.worksheet.write('C4', self.proyecto)
        self.worksheet.write('C5', self.elemento)
        self.worksheet.write('C6', self.autor)
        
    def cuadro_tabla(self):
        
        if self.cuadro == 'Cintas':
            
            self.cabecero_tabla = self.cabecero_tabla_cinta
            self.punto_tabla = self.punto_tabla_cinta
            self.n_puntos_tabla = self.n_puntos_tabla_cinta
        
        else:
            
            self.cabecero_tabla = self.cabecero_tabla_maquina
            self.punto_tabla = self.punto_tabla_maquina
            self.n_puntos_tabla = self.n_puntos_tabla_maquina
        
    def idioma_tabla(self):
        
        if self.idioma == 'Español':
            
            idm = 0
            
        elif self.idioma == 'Inglés':
            
            idm = 1
            
        else:
            
            idm = 2
            
        self.cabecero = self.cabecero_tabla[idm]
        self.punto = self.punto_tabla[idm]
        self.n_puntos = self.n_puntos_tabla[idm]
        self.combinaciones = self.combinaciones_tabla[idm]
        print(self.cabecero, self.punto, self.n_puntos, self.combinaciones)
            
        return [self.cabecero, self.punto, self.n_puntos, self.combinaciones]
        
    def filas_columnas_tabla(self):
        
        self.idm_tbl = self.idioma_tabla()
        cabecero = self.idm_tbl[0]
        punto = self.idm_tbl[1]
        n_puntos = self.idm_tbl[2]
        combinaciones = self.idm_tbl[3]
        
        if self.filas_columnas == 'Puntos/Grupos':
            
            self.worksheet.write(self.i, self.j, cabecero)
            self.worksheet.write(self.i + 1, self.j, punto)
            self.worksheet.write(self.i + 1, self.j + 1, n_puntos)
            
        else:
            
            self.worksheet.write(self.i, self.j, combinaciones)

    def filas_tabla(self):
        
        if self.filas_columnas == 'Puntos/Grupos':
        
            for key in self.apoyos.keys():
                
                self.lst_apoyos.append(key)
                
            self.worksheet.write_column(self.i + 3, self.j, self.lst_apoyos)
    
        
        
        
        
    def cierra_libro(self):
        
        self.workbook.close()
#        os.system(r'start excel.exe {}'.format(self.archivo_xlsx))
        

            