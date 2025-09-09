def main():
    # Showcase default parameter
    hello()
    # Prompt for and accept user input
    name = input("What's your name? ")
    hello(name)

# Define a function to say hello
# Set the parameter user to be "world" by default
def hello(user="world"):
    print("hello,", user)


main()