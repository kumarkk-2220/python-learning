# File Writing Examples
example_file = open("files/example_text_file.txt", 'w')
example_file.writelines(["Hi\n", "I\n", "Am\n", "Kp\n"])
example_file.close()

# File Reading Examples
example_file = open("files/example_text_file.txt", 'r')
print("Read Lines", example_file.readlines())
print("Readline", example_file.readline())
print("Read", example_file.read())
