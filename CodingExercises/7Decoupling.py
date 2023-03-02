feets_and_inches = input("Enter your height in feets and inches: ")


def height_to_meters(feets_and_inches):
    parts = feets_and_inches.split(" ")
    feet = float(parts[0])
    inch = float(parts[1])
    meters = feet * 0.3048 + inch * 0.0254
    return {"feet": feet, "inch": inch, "meters": meters}


print(f"Feet: {height_to_meters(feets_and_inches)['feet']}")
print(f"Inch: {height_to_meters(feets_and_inches)['inch']}")
print(f"Meters: {height_to_meters(feets_and_inches)['meters']}")

if height_to_meters(feets_and_inches)['meters'] < 1:
    print(f"The height is {height_to_meters(feets_and_inches)['meters']}. You can't slide")
else:
    print(f"The height is {height_to_meters(feets_and_inches)['meters']}. You can slide")
