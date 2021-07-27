# -*- coding: utf-8 -*-
"""
The QFileDialog class provides a dialog that allow users to select files or
directories.
https://www.riverbankcomputing.com/static/Docs/PyQt4/qfiledialog.html

Created on Mon Nov 18 08:28:56 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""

from PyQt5.QtWidgets import QFileDialog


class FileDialog:
    """
    La clase QFileDialog proporciona un cuadro de diálogo que permite
    seleccionar archivos o directorios.
    """

    def __init__(self, subtitulo, directorio='', filtro=''):
        self.subt = subtitulo
        self.dir = directorio
        self.ftr = filtro

    def get_existing_directory(self):
        """Devuelve una cadena de texto con la ruta."""

        ruta = QFileDialog.getExistingDirectory(
                caption=self.subt,
                directory=self.dir,
                options=QFileDialog.ShowDirsOnly
                )

        return ruta

    def get_open_file_name(self):
        """Devuelve una cadena de texto con la ruta y el nombre del fichero."""

        ruta_nombre_fichero = QFileDialog.getOpenFileName(
                caption=self.subt,
                directory=self.dir,
                filter=self.ftr
                )

        return ruta_nombre_fichero[0]

    def get_save_file_name(self):
        """Devuelve una cadena de texto con la ruta y el nombre del fichero."""

        ruta_nombre_fichero = QFileDialog.getSaveFileName(
                caption=self.subt,
                directory=self.dir,
                filter=self.ftr
                )

        return ruta_nombre_fichero[0]
