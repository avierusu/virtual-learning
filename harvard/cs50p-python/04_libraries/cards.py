import random

cards = ["jack", "queen", "king"]

def main():
    # choices() randomly selects k amount
    # of items from a list
    # There can be duplicates
    # print(random.choices(cards, k=2))

    # sample() does the same, but without
    # replacement, so no duplicates
    print(random.sample(cards, k=2))


main()