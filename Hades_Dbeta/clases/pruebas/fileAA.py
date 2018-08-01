# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:22:13 2018

@author: pc175
"""

import sys
from PyQt4 import QtGui, QtCore

import fileBB


class MyApp(fileBB.MyAppBB, QtGui.QMainWindow):
    
    def __init__(self, val):
        
        fileBB.MyAppBB.__init__(self, val)
        self.MyMethod()


if __name__ == '__main__':
    
    f = MyApp(5)
     