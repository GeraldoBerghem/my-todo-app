"""
A ordem em que colocamos as chamadas st.title, st.subheader, st...
afeta o resultado da página.
Cada vez que um refresh de tela é executado no browser,
o código python é executado novamente. Para apps com muitos usuários, é
importante que se tenha recursos computacional adequado (webscale).
Performance pode ser um issue
"""


import streamlit as st
import functions as fu

todos = fu.get_todos()
chkboxkey = 0

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if len(todo) > 1:
        todos.append(todo)
        fu.write_todos(todos)

def complete_todo(todo_arg):

    todos.remove(todo_arg)
    fu.write_todos(todos)
    del st.session_state[todo_arg]
    st.experimental_rerun()


st.title("My Todo App")
st.subheader("App to mantain todo list updates")
st.write("this app is to increase your productivity")


for todo in todos:
    chkbox = st.checkbox(todo, key=todo)
    if chkbox:
        complete_todo(todo)


st.text_input(label="Enter a todo:", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")
