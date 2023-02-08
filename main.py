print("Making a ToDo app using Python")

todo_list = []

while True:
    user_input = input("Type add, show, edit or exit: ").strip().lower()

    match user_input:
        case 'add':
            todo_item = input("Enter a ToDo item: ")
            todo_list.append(todo_item)
        case 'show':
            for item in todo_list:
                print(item.title())
        case 'exit':
            print("Now your ToDo items are :")
            for item in todo_list:
                print(item.title())
            break
        case 'edit':
            for item in todo_list:
                print(item)
            edit_item_number = int(input("Now select the item number you want to edit: ")) - 1
            new_edited_item = input("Enter a new item name: ")
            todo_list[edit_item_number] = new_edited_item
            print("The new edited item is ", new_edited_item)
            for item in todo_list:
                print(item)
        case _:
            print("Unknown command received")

print("Good Bye!, End of ToDo")
