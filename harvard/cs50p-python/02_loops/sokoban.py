# Demonstrate list functions

def main():
    history = []

    while True:
        action = input("Action: ").title()

        if action == "Undo":
            if len(history) == 0:
                print("Nothing to undo.")
            else:
                undone = history.pop()
                print(f"Undone: {undone}")
        elif action == "Restart":
            history.clear()
        else: 
            history.append(action)
        

        print(history)


main()