# Generate a random number between two numbers
import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_range = random.randint(lower_bound, upper_bound+1)
random_int = random.randrange(lower_bound, upper_bound)
print(random_range)
print(random_int)
