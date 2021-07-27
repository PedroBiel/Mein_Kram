# -*- coding: utf-8 -*-
"""
The QInputDialog class provides a simple convenience dialog to get a single
value from the user.
https://www.riverbankcomputing.com/static/Docs/PyQt4/qinputdialog.html

Created on Fri Jan 10 13:32:30 2020

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""

from PyQt5.QtWidgets import QInputDialog, QLineEdit


class InputDialogGetDouble:
    """
    La clase QInputDialog.getDouble obtiene un valor flotante del usuario.
    """
    
    def __init__(
            self,
            titulo='Decimal',
            etiqueta='Valor:',
            valor_defecto=0,
            maximo=10,
            minimo=-10,
            paso=1
            ):
        self.titulo = titulo
        self.etiqueta = etiqueta
        self.valor_defecto = valor_defecto
        self.maximo = maximo
        self.minimo = minimo
        self.paso = paso
    
    def get_double(self):
        double, ok = QInputDialog.getDouble(
            self.titulo,
            self.etiqueta,
            self.valor_defecto,
            self.minimo,
            self.maximo,
            self.paso
            )
        
        if ok and double:

            return double


class InputDialogGetInt:
    """
    La clase QInputDialog.getInt obtiene un valor entero del usuario.
    """
    
    def __init__(
            self,
            titulo='Entero',
            etiqueta='Valor:',
            valor_defecto=0,
            maximo=10,
            minimo=-10,
            paso=1
            ):
        self.titulo = titulo
        self.etiqueta = etiqueta
        self.valor_defecto = valor_defecto
        self.maximo = maximo
        self.minimo = minimo
        self.paso = paso
    
    def get_int(self):
        integer, ok = QInputDialog.getInt(
            self.titulo,
            self.etiqueta,
            self.valor_defecto,
            self.minimo,
            self.maximo,
            self.paso
            )
        
        if ok and integer:

            return integer


class InputDialogGetItem:
    """
    La clase QInputDialog.getItem permite seleccionar un item de una lista de
    strings.
    """

    def __init__(
            self,
            titulo='Texto',
            etiqueta='Cadena:',
            lista=['a', 'b', 'c'],
            actual=0,
            editable=False
            ):
        self.titulo = titulo
        self.etiqueta = etiqueta
        self.lista = lista
        self.actual = actual
        self.editable = editable

    def get_item(self):
        item, ok = QInputDialog.getItem(
            self.titulo,
            self.etiqueta,
            self.lista,
            self.actual,
            self.editable
            )

        if ok and item:

            return item


class InputDialogGetText:
    """La clase QInputDialog.getText obtiene una cadena del usuario."""
    
    def __init__(self, titulo='Texto', etiqueta='Cadena:'):
        self.titulo = titulo
        self.etiqueta = etiqueta
    
    def get_text(self):
        text, ok = QInputDialog.getText(
            self,
            self.titulo,
            self.etiqueta,
            QLineEdit.Normal,
            ''
            )
        
        if ok and text:

            return text




