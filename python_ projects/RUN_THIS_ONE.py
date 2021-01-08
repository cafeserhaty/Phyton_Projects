# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from ProjectPy import *



def main():
    numerical_calculations=QApplication(sys.argv)
    window=QMainWindow()
    ui=Ui_Dialog()
    ui.setupUi(window)
    window.show()
    sys.exit(numerical_calculations.exec_())

main()

