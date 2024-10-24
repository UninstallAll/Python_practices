import streamlit as st
import functions_new

todos = functions_new.read_todos_doc()
def add_todo():
    todo = st.session_state['new_todo']
    todo = todo + '\n'
    todos.append(todo)
    functions_new.write_todos_doc(todos)



st.title('A fucking todo app')
st.subheader('I said this is just a fucking todo app')
st.write('there is no fucking ending')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key= todo)
    if checkbox:
        todos.pop(index)
        functions_new.write_todos_doc(todos)
        del st.session_state[todo]
        st.rerun()

    # print(type(checkbox))

st.text_input(label='Enter a shit here:', placeholder='Enter a shit here:',
              on_change=add_todo, key = 'new_todo')

# st.session_state