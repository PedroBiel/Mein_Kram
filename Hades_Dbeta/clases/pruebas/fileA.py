# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:22:13 2018

@author: pc175
"""

import sys
from PyQt4 import QtGui, QtCore
#from gui1 import Ui_MainWindow
import fileB

class MyApp(fileB.MyAppB, QtGui.QMainWindow):
  def __init__(self):
     self.MyMethod()
     # Should print 'foo'


if __name__ == '__main__':
    
    f = MyApp()
     