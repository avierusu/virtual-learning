# Determine what Harry Potter house you are from
# depending on your name

name = input("What is your name? ")

# We can use match, which is like switch in other programming languages
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        # case _ serves as a default if no other case matches
        print("Who?")