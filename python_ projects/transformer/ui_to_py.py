from PyQt5 import uic

with open('ProjectPy.py','w', encoding='utf-8') as fout:
    uic.compileUi('Project.ui', fout)
