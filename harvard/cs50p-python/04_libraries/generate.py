# This program will demonstrate using the random library
# Using import will import everything from the random module
# This also means we have to use random.function()
import random
# Or we can import a specific function
# from random import choice

# choice() chooses a random item from a list
coin = random.choice(["heads", "tails"])
print(coin)

# randint() chooses an integer between a range, inclusively
die_roll = random.randint(1, 6)
print(die_roll)

# shuffle() will randomly reorder items
cards = ["ace", "two", "three", "four", "five", "six", "seven",
         "eight", "nine", "ten", "jack", "queen", "king"]
random.shuffle(cards)
print(cards)