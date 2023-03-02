check_list = {}

user_password = input("Input your password here: ")

# checking the length
length_check = False
if len(user_password) >= 8:
    length_check = True

check_list["length"] = length_check


# Checking the capital case
capital_check = False
for caps in user_password:
    if caps.isupper():
        capital_check = True

check_list["capitals"] = capital_check

# Checking the numbers
digit_check = False
for digit in user_password:
    if digit.isdigit():
        digit_check = True

check_list["digit"] = digit_check

count_true = list(check_list.values()).count(True)

if count_true == 3:
    print("Password looks great")
elif count_true in (1, 2):
    print("Password look okay. But not accepted")
else:
    print("Password should contain one small, one caps and one letter at least")
