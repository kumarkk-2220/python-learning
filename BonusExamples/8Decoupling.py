feet_inches = input("Enter feet and inches: ")


def feet_to_meters(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inch = float(parts[1])

    meters = feet * 0.3048 + inch * 0.0254
    return meters


try:
    result = feet_to_meters(feet_inches)

    if result < 1:
        print("Kid is too small!")
    else:
        print("Kid can use the slide")
except ValueError:
    print("Enter the feet and inches in this format feet<single space>inches. Example: 5 12")
