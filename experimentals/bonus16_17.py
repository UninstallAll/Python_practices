import FreeSimpleGUI as fsg

from experimentals.Bonus17_zipCreator import make_archive

label1 = fsg.Text('Select files to compress')
input1 = fsg.Input()
choose_button1 = fsg.FilesBrowse('Choose', key = 'files')

label2 = fsg.Text('Select destination')
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse('Choose',key = 'folder')

compress_button = fsg.Button('Compress')

windows = fsg.Window('File Compressor',
                     layout=[[label1, input1, choose_button1],
                             [label2, input2, choose_button2],
                             [compress_button]])

while True:
    event, values = windows.read()
    print(event, values)
    filepath = values['files'].split(";")
    folderpath = values['folder']
    print(filepath, type(filepath))
    print(folderpath,type(folderpath))
    make_archive(filepath, folderpath)

windows.close()