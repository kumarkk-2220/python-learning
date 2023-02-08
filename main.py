print("Making a ToDo app using Python")

todo_list = []

while True:
    user_input = input("Type add, show or exit: ").strip()

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
        case _:
            print("Unknown command received")

print("Bye!")

