file_names = ["1.Doc", "2.Report", "1. Presentation"]

# replace the '.' from the list items in above list & append '.txt' to it

file_names = [filename.replace(".", "-") + ".txt" for filename in file_names]

print(file_names)

new = [i for i in ['a', 'b', 'c']]
print(new)