while True:
    actions = ["add", "edit", "show", "delete"]
    operations = ["to add an item", "to delete an item", "to the added list of items", "to delete an item"]

    for action, operation in zip(actions, operations):
        print(f"{action.title()} - {operation.title()}")

    user_choice = input("select any one of the above operations: ").strip().lower()

    if user_choice == "add":
        todo_item = input("Enter a ToDo item: ") + "\n"

        # First reading the existing lines
        file = open('practice-todos.txt', 'r')
        todo_list = file.readlines()
        # Close the worked file
        file.close()

        todo_list.append(todo_item)

        # Adding Files feature External file that stores the To-Do list
        # New list is overwriting the existing one. Hence, first read the file and append to the existing list
        file = open('practice-todos.txt', 'w')
        file.writelines(todo_list)
        file.close()
    elif user_choice == "show":
        file = open("practice-todos.txt", 'r')
        todos_file = file.readlines()
        file.close()
        for index, item in enumerate(todos_file):
            print(f"{index+1}-{item}")
            file.close()
    elif user_choice == "edit":
        file = open("practice-todos.txt", 'r')
        todo_list = file.readlines()
        file.close()
        for index, item in enumerate(todo_list):
            print(f"{index + 1}-{item.title()}")
        edit_item_number = int(input("Now select the item number you want to edit: ")) - 1
        new_edited_item = input("Enter a new item name: ")
        todo_list[edit_item_number] = new_edited_item
        print("The new edited item is ", new_edited_item)
        for item in todo_list:
            print(item)
    elif user_choice == "delete":
        file = open("practice-todos.txt", 'r')
        todo_list = file.readlines()
        file.close()
        for index, item in enumerate(todo_list):
            print(f"{index + 1}-{item.title()}")
        removing_item = int(input("Enter the item number you want to remove"))
        todo_list.pop(removing_item-1)
    else:
        print("Invalid operation")
        break
