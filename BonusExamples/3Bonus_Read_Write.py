contents = ["All carrots to be cut vertically", "The carrots were reportedly sliced", "The slicing was well done"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for filename, content in zip(filenames, contents):
    file = open(f'{filename}', 'w')
    file.write(content)

file = open('logs.txt', 'w')
file.write('101.102.103.222 GET 01.988')
file.write('171.131.104.108 POST 2.143')
file.close()

file = open('logs.txt', 'r')
print(file.read())
