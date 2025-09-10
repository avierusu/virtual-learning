# Create a dictionary with spacecraft names
# as keys and their distances as values

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}


def main():
    # dict.keys() returns a list of all keys
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU away from Earth")
    
    print()
    # dict.values() returns a list of all values
    for distance in distances.values():
        print(f"{distance} in AU is {convert(distance)} m")

def convert(au):
    return au * 149597870700


main()