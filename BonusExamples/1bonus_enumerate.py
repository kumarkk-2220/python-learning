a = [('0', 'a'), ('1', 'b'), ('2', 'c')]

for i, j in a:
    print(f"{i} {j}")

# Converting a string into the list
b = enumerate("String")
print(list(b))

c = "string"
print(list(c))

# enumerate list in alphabetical order
waiting_list = ["Sen", "Ben", "John"]
waiting_list.sort()
for index, name in enumerate(waiting_list):
    print(f"{index+1}.{name}")

ips = ['100.122.133.105', '100.122.133.111']

user_input = int(input("Enter an index: "))
print(ips[user_input])

buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)