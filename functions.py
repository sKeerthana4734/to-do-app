FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads todos from the text file and returns a list of todos"""
    with open(filepath, 'r') as file:
        todos_arg = file.readlines()
    return todos_arg


def write_todos(todos_arg, filepath=FILEPATH):
    """Writes the updated todos list to the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Running functions Module")
