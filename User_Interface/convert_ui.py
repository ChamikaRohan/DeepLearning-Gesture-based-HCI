import os

from PyQt6.uic import compileUi

ui_file = 'User_Interface.ui'
py_file = 'User_Interface.py'

with open(ui_file, 'r') as ui_file_handler:
    with open(py_file, 'w') as py_file_handler:
        compileUi(ui_file_handler, py_file_handler, execute=False)

