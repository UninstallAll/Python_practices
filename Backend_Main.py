# todos = ['sdafasd','!@#$%^','1234567','ASDFFGHGJH']
# todos = []

from functions_new import read_todos_doc,write_todos_doc
#import functions
import time

now = time.strftime('%Y-%m-%d %H:%M:%S')
print('Now is', now)
print('Now is', now)

while True:
    user_action = input('type add, show, finish or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # todos = functions.read_todos_doc()
        todos = read_todos_doc()
        # with open('files/todos.txt', 'r') as file:
        #     todos = file.readlines()

        todos.append(todo + '\n')
        print('add stuff successed!')

        # file = open('files/todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        write_todos_doc(todos,'files/todos.txt')

        # with open('files/todos.txt', 'w') as file:
        #     file.writelines(todos)

    elif user_action.startswith('show') :
        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        todos = read_todos_doc()

        # #1 delete the \n of each line in the todos file
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        #2 another method
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            #3 another method
            item = item.strip('\n')
            print(f'{index+1}-{item}')
        print(f'you have {index + 1} of shit in the list'.title())
        #print(len(todos))

    elif user_action.startswith('edit') :
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = read_todos_doc()
            # with open('files/todos.txt', 'r') as file:
            #     todos = file.readlines()
            #     # todos = todos.strip('\n')
            #     print('Here is the shit that you wrote',todos)

            new_todo = input("Change to what shit?")
            todos[number] = new_todo + '\n'

            write_todos_doc(todos,'files/todos.txt')

            print('Here is the shit that you changed',new_todo)
        except ValueError:
            print('this is a fucking shit you inputed')
            continue


    elif user_action.startswith('finish') :
        try:
            number = int(user_action[6:])

            todos = read_todos_doc()

            number = number - 1
            removed = todos[number]

            todos.pop(number)

            write_todos_doc(todos,'files/todos.txt')

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f'{index+1}-{item}')

            message = f'the shit {removed.strip('\n')} has been deleted!'
            print(message)

        except IndexError:
            print('There is no this fucking number!')

    elif user_action.startswith('exit') :
        break

    else :
        print('Are you stupid?')

print('done motherfucker')