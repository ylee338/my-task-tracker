FILEPATH = 'todos.txt'
def get_todo(filepath = FILEPATH):
    """Read text file and return a list of to do"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath = FILEPATH):
    """Write to do list into txt file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print('Hello')
    print(get_todo())
