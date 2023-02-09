user_todo_list = []

while True:
    user_input = input("What you want to do: Add, Edit, Show or Exit: ").strip().lower()

    match user_input:
        case 'add':
            todo_item = input("Enter your todo item: ").title()
            user_todo_list.append(todo_item)
            user_input
        case 'show':
            for item in user_todo_list:
                print(item)
        case 'exit':
            print("Items in your list are: ")
            for item in user_todo_list:
                print(item)
            break
        case 'edit':
            print("Items in your list are: ")
            for item in user_todo_list:
                print(item)
            modify_item_number = int(input("Select the item number you want to modify: ")) - 1
            modify_item_name = input("Enter the modified name: ").title()
            user_todo_list[modify_item_number] = modify_item_name
        case _:
            print("Please select a valid action")

print("============================================")
