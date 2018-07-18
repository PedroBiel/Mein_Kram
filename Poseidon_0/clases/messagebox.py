# -*- coding: utf-8 -*-
"""
Created on Wed May 23 09:24:15 2018
@author: P. Biel
"""

from PyQt4.QtGui import QMessageBox


class MessageBox:

    def __init__(self, icono, mensaje):
        """
        icono :   'Question', 'Information', 'Warning', 'Critical'.
        mensaje : 'Texto del mensaje.'
        """

        self.icono = icono
        self.mensaje = mensaje
        self.msg = QMessageBox()

    def show_message_box(self):

        self.msg = QMessageBox()

        if self.icono == 'Question':

            self.msg.setIcon(QMessageBox.Question)
            self.msg.setWindowTitle('¡Atención, pregunta!')

        elif self.icono == 'Information':

            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle('¡Información importante para el usuario!')

        elif self.icono == 'Warning':

            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setWindowTitle('¡Atención!')

        elif self.icono == 'Critical':

            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setWindowTitle('¡Punto crítico!')

        self.msg.setText(self.mensaje)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()


if __name__ == '__main__':

    msgbox = MessageBox('Warning', 'Esto es un aviso.!')
    msgbox.show_message_box()