while True:
    user_selection = input("Type add, edit, show, complete or exit: ").strip().lower()

    if user_selection.startswith("add"):
        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        todos.append(user_selection[4:] + "\n")

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_selection.startswith("edit"):
        try:
            user_edit = int(user_selection[5:])

            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            new_item = input("Enter the new item name")
            todos[user_edit - 1] = new_item + "\n"

            with open("todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
    elif user_selection.startswith("show"):
        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        todos = [item.strip("\n") for item in todos]

        for index, todo in enumerate(todos):
            print(f"{index+1}-{todo}")
    elif user_selection.startswith("complete"):
        try:
            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            completed_item = int(user_selection[8:])
            todos.pop(completed_item - 1)
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("No items with that number")
            continue
    elif user_selection.startswith("exit"):
        print("Users exits from the prompts")
        break
    else:
        print("Invalid option selected")
