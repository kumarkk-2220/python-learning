def feet_to_meters(feet, inch):
    feet_meters = float(feet) / 3.281
    inch_meters = float(inch) / 39.37
    meters = feet_meters + inch_meters
    return round(meters, 3)
