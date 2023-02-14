print("Making a ToDo app using Python")

while True:
    user_input = input("Type add, show, edit, complete or exit: ").strip().lower()

    match user_input:
        case 'add':
            todo_item = input("Enter a ToDo item: ") + "\n"

            # First reading the existing lines
            file = open('todos.txt', 'r')
            todo_list = file.readlines()
            # Close the worked file
            file.close()

            todo_list.append(todo_item)

            # Adding Files feature External file that stores the To-Do list
            # New list is overwriting the existing one. Hence, first read the file and append to the existing list
            file = open('todos.txt', 'w')
            file.writelines(todo_list)
            file.close()

        case 'show':
            # Adding enumerate
            # Adding Fstrings
            # Opening the file in read mode here
            file = open("todos.txt", 'r')
            todo_list = file.readlines()
            file.close()

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
            file = open("todos.txt", 'r')
            todo_list = file.readlines()
            file.close()

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
            file = open("todos.txt", 'r')
            todo_list = file.readlines()
            file.close()

            # # Stripping spaces between the items - using the 'for' loop
            # new_todos = []
            #
            # for item in todo_list:
            #     new_todos.append(item.strip('\n'))

            # Stripping the extra spaces or lines using list comprehensions
            new_todos = [item.strip("\n") for item in todo_list]

            for index, item in enumerate(new_todos):
                print(f"{index + 1}-{item.title()}")

            edit_item_number = int(input("Now select the item number you want to edit: ")) - 1
            new_edited_item = input("Enter a new item name: ")
            todo_list[edit_item_number] = new_edited_item
            print("The new edited item is ", new_edited_item)
            for item in todo_list:
                print(item)

        # Adding "Complete" feature for the To-Do
        case 'complete':
            print("Your list is as follows")
            file = open("todos.txt", 'r')
            todo_list = file.readlines()
            file.close()

            # Stripping spaces between the items - using the 'for' loop
            new_todos = []

            for item in todo_list:
                new_todos.append(item.strip('\n'))

            for index, item in enumerate(new_todos):
                print(f"{index + 1}-{item.title()}")

            complete_number = int(input("Enter the number of the list item to be completed: "))
            todo_list.pop(complete_number - 1)

        case _:
            print("Unknown command received")

print("Good Bye!, End of ToDo")
   