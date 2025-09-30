# This program will open a file and read and print out
# each line in the file

# Create an empty list to store and sort the names
names = []

# We use r to only read the file
# You don't have to specify it though, it's the default
with open("names.txt") as file:
    # readlines() reads every line in the file
    # and stores them as a list
    #lines = file.readlines()
    
    # We can instead read the lines and print them out
    # all at the same time
    # However, if we do this, we cannot sort the names
    for line in file:
        # We use rstrip() to remove the new line character
        # that is automatically at the end of each line in
        # the file
        # print("Hello,", line.rstrip())

        # Instead, we will store each name into our own list
        # to then sort and print
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")