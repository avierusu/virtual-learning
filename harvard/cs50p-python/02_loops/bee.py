# Spelling bee sorta
# The user will spell words from a list of letters
# and get points depending on how long the word is

WORDS = {
    "PAIR": 4,
    "HAIR": 4,
    "CHAIR": 5,
    "CHAR": 4,
    "CRAG": 6,
    "GRAPHIC": 7
}

def main():
    print("Welcome to the Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ").upper()

        # If the user guesses the super word, end the game immediately
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!!!")

        # Check if the guessed word is in the dictionary of words
        if guess in WORDS.keys():
            # Pop returns the value of a key, and then removes
            # the key/value pair
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points!")

    
    print("\nThat's the game!")


main()