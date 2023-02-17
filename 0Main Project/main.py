print("Making a ToDo app using Python")

while True:
    user_input = input("Type add, show, edit, complete or exit: ").strip().lower()

    if 'add' in user_input:
        todo_item = user_input[4:] + "\n"

        # First reading the existing lines
        # adding 'with' context manager
        with (open('todos.txt', 'r')) as file:
            todo_list = file.readlines()

        todo_list.append(todo_item)

        # Adding Files feature External file that stores the To-Do list
        # New list is overwriting the existing one. Hence, first read the file and append to the existing list

        # Adding with context manager
        with (open('todos.txt', 'w')) as file:
            file.writelines(todo_list)

    elif 'show' in user_input:
        # Adding enumerate
        # Adding Fstrings
        # Opening the file in read mode here
        with (open('todos.txt', 'r')) as file:
            todo_list = file.readlines()

        # # Stripping spaces between the items - using the 'for' loop
        # new_todos = []
        #
        # for item in todo_list:
        #     new_todos.append(item.strip('\n'))

        # Stripping the extra spaces or lines using list comprehensions
        new_todos = [item.strip("\n") for item in todo_list]

        for index, item in enumerate(new_todos):
            print(f"{index + 1}-{item.title()}")

    elif 'exit' in user_input:
        print("Now your ToDo items are :")
        with (open('todos.txt', 'r')) as file:
            todo_list = file.readlines()

        # # Stripping spaces between the items - using the 'for' loop
        # new_todos = []
        #
        # for item in todo_list:
        #     new_todos.append(item.strip('\n'))

        # Stripping the extra spaces or lines using list comprehensions
        new_todos = [item.strip("\n") for item in todo_list]

        for index, item in enumerate(new_todos):
            print(f"{index + 1}-{item.title()}")
        break

    elif 'edit' in user_input:
        # Reading the file first
        with (open('todos.txt', 'r')) as file:
            todo_list = file.readlines()

        edit_item_number = int(user_input[5:]) - 1
        print(edit_item_number)
        new_edited_item = input("Enter a new item name: ")
        todo_list[edit_item_number] = new_edited_item + "\n"

        with (open('todos.txt', 'w')) as file:
            file.writelines(todo_list)

    # Adding "Complete" feature for the To-Do
    elif 'complete' in user_input:
        with (open("todos.txt", 'r')) as file:
            file.readlines()

        complete_number = int(user_input[9:]) - 1
        todo_to_remove = todo_list[complete_number].strip("\n")
        todo_list.pop(complete_number)

        with (open("todos.txt", 'w')) as file:
            file.writelines(todo_list)

        print(f"Your todo item {todo_to_remove} has been removed")

    else:
        print("Unknown command received")

print("Good Bye!, End of ToDo")
