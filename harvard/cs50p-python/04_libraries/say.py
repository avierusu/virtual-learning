# This program will import methods from our own
# custom library
import sys

# Import our function hello
from sayings import goodbye
# Also when we import our library,
# It will automatically run the main function


if len(sys.argv) == 2:
    goodbye(sys.argv[1])