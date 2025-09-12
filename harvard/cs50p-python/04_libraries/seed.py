import random

cards = [
    "ace",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "jack",
    "queen",
    "king"
]

def main():
    # We can use seed() to simulat pseudo-randomness;
    # while we will generate random cards, each time
    # we run the program, the "random" cards will be
    # the same every time
    # Normally the seed changes based on system time,
    # making the seed different every time you run
    # the program and making the random selections
    # different every time
    random.seed(0)
    print(random.choices(cards, k=5))


main()