from cProfile import label
import functions_new

import FreeSimpleGUI as fsg

label = fsg.Text('Type in a todo thing')
input_box = fsg.InputText(tooltip='Enter a todo', key ='todo')
add_button = fsg.Button('Add')
list_box = fsg.Listbox(values = functions_new.read_todos_doc(),
                       key = 'todos', enable_events = True,
                       size = [45,10])
edit_button = fsg.Button('Edit')

windows = fsg.Window('A FUCKING TODO APP',
                     layout=[[label],[input_box,add_button],[list_box,edit_button]],
                     font = ('Helvetica',15))

while True:
    event, values = windows.read()
    print(f'event: {event}')
    print(f'values: {values}')
    # print(f'values_todos: {f'{values['todos']}'}')
    print(f"values_todos: {values['todos']}")

    match event:
        case 'Add':
            todos = functions_new.read_todos_doc()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions_new.write_todos_doc(todos)
            windows['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']+ '\n'

            todos = functions_new.read_todos_doc()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions_new.write_todos_doc(todos)
            windows['todos'].update(values = todos)

        case 'todos':
            windows['todo'].update(value = values['todos'][0])


        case fsg.WINDOW_CLOSED:
            break

windows.close()