user_password = input("Enter your password: ")

# Length has to be 8 character at least
# one small case character should be there
# At least one number should be there
password_checklist = {}

if len(user_password) >= 8:
    password_checklist['length'] = True
else:
    password_checklist['length'] = False

digit_check = False
for character in user_password:
    if character.isdigit():
        digit_check = True

password_checklist['digit'] = digit_check

upper_check = False
for character in user_password:
    if character.isupper():
        upper_check = True

password_checklist['upper'] = upper_check

print(password_checklist)
print(all(password_checklist))

true_count = list(password_checklist.values()).count(True)

if true_count >= 3:
    print("Strong Password")
elif true_count in (0, 2):
    print("Password looks OK!, Can be improved")
else:
    print("Weak Password")
