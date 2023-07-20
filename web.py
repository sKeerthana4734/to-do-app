import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo", placeholder="Add new todo...")