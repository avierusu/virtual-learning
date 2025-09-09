def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

# Define a function to square an integer
def square(num):
    return num * num
    # We can also raise num to various powers by using one of the following methods
    # num ** 2
    # pow(num, 2)


main()