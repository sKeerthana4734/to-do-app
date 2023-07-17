import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S %p")
print("Date and Time: ", now)

while True:
    user_action = input("Type add, show, edit, complete or exit:  ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)
        print("Todo added successfully!")

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        print("\nThe current todos are:")
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item.capitalize()}")
        print()

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1
            todos = functions.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)
            print(f"Todo edited successfully!")

        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            completed_todo = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            print(f"Todo '{completed_todo}' was removed from the list!")

        except IndexError:
            print("Invalid todo number")
            continue

    elif user_action.startswith('exit'):
        print("See yaah!")
        break

    else:
        print("Please enter a valid option!")
