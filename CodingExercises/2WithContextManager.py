while True:
    with open("coin_flip.txt", "r") as file:
        sides = file.readlines()

    user_choice = input("Heads or Tails?: ")

    sides.append(user_choice + "\n")

    with open("coin_flip.txt", 'w') as file:
        file.writelines(sides)

    heads_count = sides.count("heads\n")

    percentage = heads_count / len(sides) * 100

    print(f"Heads probability: {percentage}")
