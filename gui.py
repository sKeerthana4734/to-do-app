import functions
import PySimpleGUI as sg

label = sg.Text("Type a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="new_todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos_list',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button, complete_button], [exit_button]],
                   font=("Helvetica", 16))

while True:
    event, values = window.read()
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['new_todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
            window["new_todo"].update(value='')
        case "Edit":
            todo = values['todos_list'][0]
            edited_todo = values['new_todo']
            todos = functions.get_todos()
            index = todos.index(todo)
            todos[index] = edited_todo + '\n'
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
        case 'todos_list':
            window['new_todo'].update(value=values['todos_list'][0])
        case "Complete":
            completed_todo = values["todos_list"][0]
            todos = functions.get_todos()
            todos.remove(completed_todo)
            functions.write_todos(todos)
            window["todos_list"].update(values=todos)
            window["new_todo"].update(value='')
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()
