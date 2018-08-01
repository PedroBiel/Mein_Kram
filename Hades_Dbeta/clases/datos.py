# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:07:02 2018

@author: pc175
"""

import pandas as pd

class Datos:
    """
    Para pasar datos entre formularios los objetos se pasan por referencia.
    """
    var = ''   # Variable (string o num).
    var1 = ''   # Variable (string o num).
    var2 = ''   # Variable (string o num).
    var3 = ''   # Variable (string o num).
    var4 = ''   # Variable (string o num).
    var5 = ''   # Variable (string o num).
    lst = []   # Lista.
    dcc = {}   # Diccionario.
    dcc1 = {}  # Diccionario1.
    df = pd.DataFrame() # DataFrame de pandas.
    