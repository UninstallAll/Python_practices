from cProfile import label
import functions_new
import FreeSimpleGUI as fsg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass

fsg.theme('Green')

label_time = fsg.Text('',key='clock')
label = fsg.Text('Type in a todo thing')
input_box = fsg.InputText(tooltip='Enter a todo', key ='todo')
add_button = fsg.Button('Add')
# add_button = fsg.Button(key = 'Add', size = 2, image_source = 'add.png',
#                         mouseover_colors= 'LightBlue2',tooltip = 'Add todo')
list_box = fsg.Listbox(values = functions_new.read_todos_doc(),
                       key = 'todos', enable_events = True,
                       size = [45,10])
edit_button = fsg.Button('Edit')
complete_button = fsg.Button('Complete')
exit_button = fsg.Button('Exit')

layout = [[label_time],
          [label],
          [input_box, add_button],
          [list_box, edit_button,complete_button],
          [exit_button]]

windows = fsg.Window('A FUCKING TODO APP',
                     layout=layout,
                     font = ('Helvetica',15))

while True:
    event, values = windows.read(timeout=200)
    windows['clock'].update(value=time.strftime('%Y-%m-%d %H:%M:%S'))
    # print(f'event: {event}')
    # print(f'values: {values}')
    # # print(f'values_todos: {f'{values['todos']}'}')
    # print(f"values_todos: {values['todos']}")


    match event:
        case 'Add':
            todos = functions_new.read_todos_doc()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions_new.write_todos_doc(todos)
            windows['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']+ '\n'

                todos = functions_new.read_todos_doc()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions_new.write_todos_doc(todos)
                windows['todos'].update(values = todos)
            except IndexError:
                fsg.popup('Please enter a item',font = ('Helvetica',15))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions_new.read_todos_doc()
                todos.remove(todo_to_complete)
                functions_new.write_todos_doc(todos)
                windows['todos'].update(values = todos)
                windows['todo'].update(value ='')
            except IndexError:
                fsg.popup('Please enter a item', font=('Helvetica', 15))

        case 'Exit':
            break


        case 'todos':
            windows['todo'].update(value = values['todos'][0])


        case fsg.WINDOW_CLOSED :
            # windows.close()
            break

windows.close()
