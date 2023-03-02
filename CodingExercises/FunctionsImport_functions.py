low = 0
high = 100


def state_of_water(temperature):
    if temperature < low:
        return "Solid"
    elif low < temperature < high:
        return "Liquid"
    else:
        return "Gas"


