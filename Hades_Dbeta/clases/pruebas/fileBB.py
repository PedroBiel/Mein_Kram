# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:22:12 2018

@author: pc175
"""

import sys
from PyQt4 import QtGui, QtCore


class MyAppBB(QtGui.QMainWindow):
    
    def __init__(self, val):
        self.val = val
        
    def MyMethod(self):
        print(self.val)
    
    
if __name__ == '__main__':
    
    f = MyAppBB(10)
    f.MyMethod()