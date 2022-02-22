new_item = input("Please enter a new to-do item: ")

# opened a file in Python and reads contents
with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()


todo = todo + new_item + '\n'

# writes input/new item to file
with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)
