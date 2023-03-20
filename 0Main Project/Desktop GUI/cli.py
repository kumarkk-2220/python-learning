# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")
while True:
    user_selection = input("Type add, edit, show, complete or exit: ").strip().lower()

    if user_selection.startswith("add"):
        todos = functions.get_todos()

        todos.append(user_selection[4:] + "\n")

        functions.write_todos(todos_arg=todos)

    elif user_selection.startswith("edit"):
        try:
            user_edit = int(user_selection[5:])

            todos = functions.get_todos()

            new_item = input("Enter the new item name: ")
            todos[user_edit - 1] = new_item + "\n"

            functions.write_todos(todos_arg=todos)
        except ValueError:
            print("Your command is not valid")
    elif user_selection.startswith("show"):
        todos = functions.get_todos()

        todos = [item.strip("\n") for item in todos]

        for index, todo in enumerate(todos):
            print(f"{index + 1}-{todo}")
    elif user_selection.startswith("complete"):
        try:
            todos = functions.get_todos()

            completed_item = int(user_selection[8:])
            todos.pop(completed_item - 1)
            functions.write_todos(todos_arg=todos)
        except IndexError:
            print("No items with that number")
            continue
    elif user_selection.startswith("exit"):
        print("Exiting from the prompts")
        break
    else:
        print("Invalid option selected")
