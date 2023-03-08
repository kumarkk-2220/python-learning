user_string = input("Enter the string that contains number in it")

digits = []
for i in user_string:
    if i.isdigit():
        digits.append(int(i))
    else:
        continue

is_digit = False
for j in digits:
    if str(j).isdigit():
        is_digit = True
    else:
        is_digit = False

if not is_digit:
    print("No numbers in your string")
else:
    print(sum(digits))
