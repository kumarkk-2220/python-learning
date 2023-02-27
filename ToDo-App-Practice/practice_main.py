while True:
    selections = ["add", "edit", "show", "complete", "exit"]
    actions = ["To add a to-do item", "To edit a to-do item", "To show the todo list", "To mark an item complete",
               "To stop"]

    for selection, action in zip(selections, actions):
        print(f"{selection} - {action}")

    user_selection = input("Choose one of the actions from above list: ").strip().lower()

    if 'add' in user_selection:
        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        todos.append(user_selection[4:] + "\n")

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

    elif 'edit' in user_selection:
        user_edit = int(user_selection[5:])

        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        new_item = input("Enter the new item name")
        todos[user_edit - 1] = new_item + "\n"

        with open("todos.txt", 'w') as file:
            file.writelines(todos)
    elif 'show' in user_selection:
        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        todos = [item.strip("\n") for item in todos]

        for index, todo in enumerate(todos):
            print(f"{index+1}-{todo}")
    elif 'complete' in user_selection:
        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        completed_item = int(user_selection[8:])
        todos.pop(completed_item - 1)
        with open("todos.txt", 'w') as file:
            file.writelines(todos)
    elif 'exit' in user_selection:
        print("Users exits from the prompts")
        break
    else:
        print("Invalid option selected")
