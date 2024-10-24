import streamlit as st
import functions_new

todos = functions_new.read_todos_doc()

st.title('A fucking todo app')
st.subheader('I said this is just a fucking todo app')
st.write('there is no fucking ending')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Enter a shit here:', placeholder='Enter a shit here:')