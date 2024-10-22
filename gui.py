from cProfile import label
import functions_new

import FreeSimpleGUI as fsg

label = fsg.Text('Type in a todo thing')
input_box = fsg.InputText(tooltip='Enter a todo', key ='todo')
add_button = fsg.Button('Add')

windows = fsg.Window('A FUCKING TODO APP',
                     layout=[[label],[input_box,add_button]],
                     font = ('Helvetica',15))

while True:
    event, values = windows.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            todos = functions_new.read_todos_doc()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions_new.write_todos_doc(todos)

        case fsg.WINDOW_CLOSED:
            break



windows.close()