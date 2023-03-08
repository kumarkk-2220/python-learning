# import glob
#
# my_txt_files = glob.glob("files/*.txt")
# my_py_files = glob.glob("*.py")
#
# for content in my_txt_files:
#     with open(content, 'r') as file:
#         print(file.read())
#


# import csv
#
# with open("weather.csv", 'r') as file:
#     data = list(csv.reader(file))
#
# city = input("Enter the city: ").title()
#
# for city_name in data[1:]:
#     if city_name[0] == city:
#         print(city_name[1])


# import shutil
# shutil.make_archive("Output", "zip", "files")

import webbrowser

user_term = input("Enter the search term").replace(" ", "+")
webbrowser.open(f"https://www.google.com/search?q={user_term}")
