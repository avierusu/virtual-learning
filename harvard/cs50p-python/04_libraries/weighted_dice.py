import random

die_sides = [1, 2, 3, 4, 5, 6]

def main():
    # The choices() function also has an argument
    # called "weights". This lets us assign weights
    # to list elements, making some more likely than
    # others
    print(random.choices(die_sides, weights=[5, 5, 5, 5, 5, 75], k=2))


main()