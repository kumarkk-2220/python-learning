# year_of_birth = int(input("Enter your birth year: "))
#
#
# def age_calculation(year_of_birth, current_year=2023):
#     age = current_year - year_of_birth
#     return age
#
#
# print(age_calculation(year_of_birth))

names = input("Enter any number of names each separated by a comma: ")


def count_names(name=names):
    names_count = name.split(",")
    return len(names_count)


print(count_names(names))
