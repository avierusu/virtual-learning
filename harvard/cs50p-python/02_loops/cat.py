# Basic loops

# While loop
counter = 0
while counter < 3:
    print("meow")
    # Python does not support ++
    counter += 1

print()
#For loop
# This version is not scaleable for large sizes
# as we have to hard code the list
for index in [0, 1, 2]:
    print("meow")

print()
# Alternatively:
# Underscore is used as the variable name because
# we don't need to know or use the variable,
# it is simply required for the loop
for _ in range(3):
    print("meow")

print()
# In python we can also just multiply in a print statement lol
print("meow\n" * 3, end="")