while True:
    choices = ["Add", "Edit", "Show", "Complete", "Exit"]
    actions = ["To Add a To-Do Item", "To Edit a To-Do Item", "To Show list", "To Complete a To-Do Item", "To Exit"]

    for choice, action in zip(choices, actions):
        print(f"{choice} {action}: ")

    user_choice = input().lower().strip()

    if 'add' in user_choice or 'new' in user_choice:
        todo_item = user_choice[4:] + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo_item)

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

    elif 'show' in user_choice:
        with open("todos.txt", 'r') as file:
            todos = file.readlines()
            todos = [item.strip("\n") for item in todos]
            for index, todo in enumerate(todos):
                print(f"{index + 1}-{todo}")
    elif 'edit' in user_choice:
        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        edit_item_name = input("Enter the new edit name")
        todos[int(user_choice[5:]) - 1] = edit_item_name + "\n"

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_choice:
        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        todos.pop(int(user_choice[9:]) - 1)

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

    elif 'exit' in user_choice:
        break
    else:
        print("Invalid command received")
