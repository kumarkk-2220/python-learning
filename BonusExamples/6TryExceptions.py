# Calculating area of a rectangle

try:
    length = float(input("Enter the value of the length: "))
    width = float(input("Enter the value of the width: "))

    if length == width:
        exit("That looks like a square")

    area = length * width
    print(area)
except ValueError:
    print("Enter the number only")
