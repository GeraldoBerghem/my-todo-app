

def get_todos(filepath="todos.txt"):
    """" reads the txt file and returns all its lines in a list """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ write the to-do items list in the txt file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":
    print("hello from functions")