# liters = float(input("Enter the number of liters"))
#
#
# def lit_cubic_lit(liters):
#     cubic_liter = liters/1000
#     return cubic_liter
#
#
# print(lit_cubic_lit(liters))
#
# user_password = input("Input your password here: ")
#
#
# def password_strength(user_password):
#     check_list = {}
#
#     # checking the length
#     length_check = False
#     if len(user_password) >= 8:
#         length_check = True
#
#     check_list["length"] = length_check
#
#
#     # Checking the capital case
#     capital_check = False
#     for caps in user_password:
#         if caps.isupper():
#             capital_check = True
#
#     check_list["capitals"] = capital_check
#
#     # Checking the numbers
#     digit_check = False
#     for digit in user_password:
#         if digit.isdigit():
#             digit_check = True
#
#     check_list["digit"] = digit_check
#
#     count_true = list(check_list.values()).count(True)
#     return count_true
#
#
# if password_strength(user_password) == 3:
#     print("Password looks great")
# elif password_strength(user_password) in (1, 2):
#     print("Password look okay. But not accepted")
# else:
#     print("Password should contain one small, one caps and one letter at least")

def speed(distance, time):
    return distance / time


print(speed(200, 4))