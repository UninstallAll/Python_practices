FILEPATH = 'files/todos.txt'

def read_todos_doc(filepath = FILEPATH):
    """Just read some shitty files"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos_doc(todos_local, filepath = FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)


print(__name__)