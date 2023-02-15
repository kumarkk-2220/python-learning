print("Making a ToDo app using Python")

while True:
    user_input = input("Type add, show, edit, complete or exit: ").strip().lower()

    match user_input:
        case 'add':
            todo_item = input("Enter a ToDo item: ") + "\n"

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

        case 'show':
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

        case 'exit':
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

        case 'edit':
            # Reading the file first
            with (open('todos.txt', 'r')) as file:
                todo_list = file.readlines()

            edit_item_number = int(input("Now select the item number you want to edit: ")) - 1
            new_edited_item = input("Enter a new item name: ")
            todo_list[edit_item_number] = new_edited_item + "\n"

            with (open('todos.txt', 'w')) as file:
                file.writelines(todo_list)

        # Adding "Complete" feature for the To-Do
        case 'complete':
            with (open("todos.txt", 'r')) as file:
                file.readlines()

            complete_number = int(input("Enter the number of the list item to be completed: "))
            todo_to_remove = todo_list[complete_number - 1].strip("\n")
            todo_list.pop(complete_number - 1)

            with (open("todos.txt", 'w')) as file:
                file.writelines(todo_list)

            print(f"Your todo item {todo_to_remove} has been removed")

        case _:
            print("Unknown command received")

print("Good Bye!, End of ToDo")
   