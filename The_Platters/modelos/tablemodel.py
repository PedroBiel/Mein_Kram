# -*- coding: utf-8 -*-
"""
DESCRIPCIÓN

Created on Fri Nov 29 09:29:13 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""

import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt


class PandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():

            if role == Qt.DisplayRole:

                return str(self._data.iloc[index.row(), index.column()])

            if (index.column() == 0 and role == Qt.TextAlignmentRole):

                return Qt.AlignHCenter | Qt.AlignVCenter

            elif (index.column() == 1 and role == Qt.TextAlignmentRole):

                return Qt.AlignHCenter | Qt.AlignVCenter

            elif (index.column() == 2 and role == Qt.TextAlignmentRole):

                return Qt.AlignHCenter | Qt.AlignVCenter

        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


if __name__ == '__main__':

    df = pd.DataFrame({'a': ['Mary', 'Jim', 'John'],
                       'b': [100, 200, 300],
                       'c': ['a', 'b', 'c']
                       })

    app = QApplication(sys.argv)
    model = PandasModel(df)
    view = QTableView()
    view.setModel(model)
    view.resize(400, 200)
    view.show()
    sys.exit(app.exec_())
