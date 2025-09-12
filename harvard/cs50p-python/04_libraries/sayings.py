# We will practice creating our own libraries in their own files

def main():
    hello("world")
    goodbye("world")



def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")


# We use this if statement so that
# when our file is imported, it will
# not immediately run the main function
# in this library file
if __name__ == "__main__":
    main()