import FreeSimpleGUI as fsg
import Bouns18_zipExtractor_functions
from experimentals.Bouns18_zipExtractor_functions import extract_archive

fsg.theme('DarkAmber')

label1 = fsg.Text('Select files to extract')
input1 = fsg.Input()
choose_button1 = fsg.FileBrowse('Choose', key = 'zipfile')

label2 = fsg.Text('Select destination')
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse('Choose',key = 'folder')

extract_button = fsg.Button('Extract')
output_label = fsg.Text(key = 'Output',text_color='green')

windows = fsg.Window('Zip File Extractor',
                     layout=[[label1, input1, choose_button1],
                             [label2, input2, choose_button2],
                             [extract_button,output_label]])

while True:
    event, values = windows.read()
    print(event, values)

    archivepath = values['zipfile']
    dest_dir    = values['folder']

    extract_archive(archivepath, dest_dir)

    windows['Output'].update(value ='Extraction Completed!')



windows.close()