# Ask user for the difficulty and number of players
# and return with the best card game recommendation

def main():
    # Prompt for difficulty
    difficulty = input("Difficult or Casual? ").capitalize()
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return
    
    players = input("Multiplayer or Single-player").capitalize()
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid number of players")
        return
    

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print("You might like", game)


main()
