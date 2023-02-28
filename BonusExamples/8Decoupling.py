feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inch = float(parts[1])
    return {"feet": feet, "inch": inch}


def feet_to_meters(feet, inch):
    meters = feet * 0.3048 + inch * 0.0254
    return meters


try:
    result = feet_to_meters(parse(feet_inches)["feet"], parse(feet_inches)["inch"])

    print(f"{parse(feet_inches)['feet']} feet and {parse(feet_inches)['inch']} inches is equal to {result}")

    if result < 1:
        print("Kid is too small!")
    else:
        print("Kid can use the slide")
except ValueError:
    print("Enter the feet and inches in this format feet<single space>inches. Example: 5 12")
