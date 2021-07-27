# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:29:39 2017

@author: P. Biel

Renombra los nombres de los ficheros contenidos en una carpeta sustituyendo las
letras en mayúsculas por minúsculas.
"""

import os

print('-----------------')
print('Learning by doing')
print('® 2017 Pedro Biel')
print('-----------------')
print()
print('upper2lower 0.0.170728')
print()
print('Renombra los nombres de los ficheros contenidos en una carpeta')
print('sustituyendo las letras en mayúsculas por minúsculas.')
print()

cwd = input('Ruta del directorio (por ejemplo C:\Python): ')

os.chdir(cwd)
os.getcwd()
list_dir = [x for x in os.listdir(cwd)]

print()
print('Lista de nombres de ficheros originales en el directorio:')
print('---------------------------------------------------------')
for ld in list_dir:
    print(ld)

for filename in os.listdir(cwd):
    os.rename(filename, filename.lower())

print()
print('Lista de nombres de ficheros modificados en el directorio:')
print('----------------------------------------------------------')
for ld in list_dir:
    print(ld)

print()
print('Listo.')
input()

    

    