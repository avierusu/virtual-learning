import sys

# We can use sys.argv to pass input when
# we run the program
# we use sys.argv[1] because sys.arg[0]
# will return the file name of the program,
# because we run python name.py input
# name.py is sys.argv[0], and whatever
# our input in is sys.argv[1] and so on
if len(sys.argv) < 2:
    # We can use sys.exit to completely
    # exit from the program
    sys.exit("Too few arguments")

# Since sys.argv[0] is the file name
# and we dont want to include that,
# We explicitly slice it to exclude it
for arg in sys.argv[1:-1]:
    print("Hello, my name is", arg)