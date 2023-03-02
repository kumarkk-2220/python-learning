names = ["john smith", "jay santi", "eva kuki"]
# Extend the code above so the code capitalizes all the names and the surnames of the list and then prints the new list.
names = [name.title() for name in names]
print(names)


usernames = ["john 1990", "alberta1970", "magnola2000"]
# Extend the code above so the code prints out a list containing the number of characters for each username
usernames_count = [len(username) for username in usernames]
print(usernames_count)

user_entries = ['10', '19.1', '20']
# Extend the code above so the code prints out a list containing the same items as floats.
user_entries1 = [float(user_entry) for user_entry in user_entries]
print(user_entries1)

user_entries = ['10', '19.1', '20']
user_numbers = [float(item) for item in user_entries]
print(sum(user_numbers))

temperatures = [10, 12, 14]

temperatures = [str(temperature) + "\n" for temperature in temperatures]
file = open("file.txt", 'w')
file.writelines(temperatures)
