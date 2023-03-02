# try:
#     total_value = int(input("Enter the total value: "))
#     value = int(input("Enter the value: "))
#     percentage = (value/total_value) * 100
#     print(f"{percentage}%")
# except ValueError:
#     exit("Enter the numbers only")


waiting_list = ["john", "marry"]
name = input("Enter name: ")

try:
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} is not in the list")

