from tkinter import image_types

import FreeSimpleGUI as fsg

label1 = fsg.Text('Select files to compress')
input1 = fsg.Input()
choose_button1 = fsg.FileBrowse('Choose')

label2 = fsg.Text('Select destination')
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse('Choose')

compress_button = fsg.Button('Compress')

windows = fsg.Window('File Compressor',
                     layout=[[label1, input1, choose_button1],
                             [label2, input2, choose_button2],
                             [compress_button]])
windows.read()
windows.close()