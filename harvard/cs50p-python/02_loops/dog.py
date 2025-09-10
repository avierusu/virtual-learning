# Loop a user defined amount of loops

def main():
    number = get_number()
    woof(number)

# Use a while loop to make sure user input is positive
def get_number():
    while True:
        n = int(input("How many loops? "))
        if n > 0:
            break
    
    return n

def woof(loops):
    for _ in range(loops):
        print("woof")


main()