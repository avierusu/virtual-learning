def main():
    print_column(3)
    print()
    print_row(4)
    print()
    print_square(3)

def print_column(height):
    print("#\n" * height, end="")

def print_row(length):
    print("?" * length)

def print_square(size):
    for row in range(size):
        print("#" * size)


main()