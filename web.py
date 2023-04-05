import streamlit as st
import functions

todos = functions.get_todo()

def add_todo():
    todo =st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)



st.title('My To-Do App')
st.write('This app is to keep track of my daily tasks.')



for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder='Enter a new task...',
              on_change=add_todo, key='new_todo')

