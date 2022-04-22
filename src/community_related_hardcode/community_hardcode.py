# Special number to map the building
HOUSE_NUMBER = 500
SPECIAL_NUMBER_1 = 5889
SPECIAL_NUMBER_2 = 9999


class Community:
    def __init__(self):
        pass

    # Every community arrange the building in some strange ways.
    # Need a mapping function to tell the code how to convert the building number to actual ones.
    def special_building_numbers(self):
        pass


def tryGetValue(x, func, default):
    try:
        return func(x)
    except:
        return default