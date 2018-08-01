# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:22:12 2018

@author: pc175
"""

import sys
from PyQt4 import QtGui, QtCore
#from gui1 import Ui_MainWindow

class MyAppB(QtGui.QMainWindow):
  def MyMethod(self):
    print('foo')
    
    
if __name__ == '__main__':
    
    f = MyAppB()
    f.MyMethod()