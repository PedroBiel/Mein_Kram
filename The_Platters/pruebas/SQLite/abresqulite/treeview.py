# -*- coding: utf-8 -*-
"""
DESCRIPCIÓN

Created on Wed Nov 20 12:56:56 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QTreeView

class Food(object):
    def __init__(self, name, shortDescription, note, parent = None):
        self.data = (name, shortDescription, note);
        self.parentIndex = parent

class FavoritesTableModel(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self)
        self.foods = []  
        self.loadData() 

    def data(self, index, role = Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.foods[index.row()].data[index.column()]
        return None

    def rowCount(self, index=QModelIndex()):
        return len(self.foods)

    def columnCount(self, index=QModelIndex()):
        return 3

    def index(self, row, column, parent = QModelIndex()):  
        return self.createIndex(row, column, parent)

    def loadData(self):   
        allFoods=("Apples", "Pears", "Grapes", "Cookies", "Stinkberries")
        allDescs = ("Red", "Green", "Purple", "Yummy", "Huh?")
        allNotes = ("Bought recently", "Kind of delicious", "Weird wine grapes",
                    "So good...eat with milk", "Don't put in your nose")
        for name, shortDescription, note in zip(allFoods, allDescs, allNotes):
            food = Food(name, shortDescription, note)                                      
            self.foods.append(food) 

def main():
    import sys
    app = QApplication(sys.argv)

    model = FavoritesTableModel() 

    #Table view
    view1 = QTableView()
    view1.setModel(model)
    view1.show()

    #Tree view
    view2 = QTreeView()
    view2.setModel(model)
    view2.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()