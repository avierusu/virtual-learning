# Showcase importing custom libraries from the internet
# using the in-line command pip
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])