# If we want to store multiple names, we can use a list
# but that list will be reset each time the program ends
# and we run it again
# This is where we can use files

name = input("What is your name? ")

# We use open() to open a file, if it exists, or create
# and open a file, if it doesnt exist
# The second parameter in open() represents the operation
# we will be using the file for
# w - write to file. This will override the existing file if
# we run it again
# a - append to file. This is what we want; we will append
# names to the end of our file each time we run the program

# open() returns a file handle, and we can assign that to a
# variable to be able to access the file
# file = open("names.txt", "a")

# Instead of opening and assigning and closing the file at the
# end like we were doing, we can use the keyword with to open
# the file and automatically close the file at the end of the
# with statement
# All code within the with statement can access the file
with open("names.txt", "a") as file:
    # Add the users input to the file
    # write() will not add any spaces or new lines after appending
    # so we must add new lines manually
    file.write(f"{name}\n")
# Now, close the file
# file.close()