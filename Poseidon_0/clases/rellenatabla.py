from PyQt4 import QtCore, QtGui


class RellenaTabla:

    def __init__(self, rows, tabla, parametros):

        self.rows = rows              # Filas de la tabla
        self.tabla = tabla            # Tabla QTableWidget.
        self.parametros = parametros  # Parámetros sísmicos.

    def rellena_tabla(self):

        self.rows += 1
        self.tabla.setRowCount(self.rows)
        row = self.rows - 1
        col = 0

        for parametro in self.parametros:

            item = QtGui.QTableWidgetItem(parametro)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tabla.setItem(row, col, QtGui.QTableWidgetItem(item))

            col += 1

        ancho_tabla = AnchoTabla(self.tabla)
        ancho_tabla.set_table_width()

    def filas(self):

        return self.rows


class AnchoTabla:

    def __init__(self, tabla):

        self.tabla = tabla

        self.tabla.setVisible(False)
        self.tabla.verticalScrollBar().setValue(0)
        # self.tabla.resizeRowsToContents()
        self.tabla.resizeColumnsToContents()
        self.tabla.setVisible(True)
        self.set_table_width()

    def set_table_width(self):

        width = self.tabla.verticalHeader().width()
        width += self.tabla.horizontalHeader().length()

        if self.tabla.verticalScrollBar().isVisible():

            width += self.tabla.verticalScrollBar().width()

        width += self.tabla.frameWidth() * 2
        self.tabla.setFixedWidth(width)
