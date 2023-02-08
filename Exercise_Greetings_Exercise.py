user_country = input("Enter the country you are from: ")

match user_country.strip().upper():
    case 'USA':
        print("Hello!")
    case 'INDIA':
        print("Namaste!")
    case 'GERMANY':
        print("Hallo")
    case _:
        print("Oh no! You are not in list of the allowed countries")


ingredients = ["john smith", "sen plakay", "dora ngacely"]
for i in ingredients:
    print(i.title())