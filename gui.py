from cProfile import label
import functions_new

import FreeSimpleGUI as fsg

label = fsg.Text('Type in a todo thing')
input_box = fsg.InputText(tooltip='Enter a todo')
add_button = fsg.Button('Add')

windows = fsg.Window('A FUCKING TODO APP', layout=[[label],[input_box,add_button]])
windows.read()
windows.close()