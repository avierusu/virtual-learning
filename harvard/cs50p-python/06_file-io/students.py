# This program will read data from a Comma-Separated
# Value (CSV) file

import csv

# Create a list to store students and their houses
students = []

with open("students.csv") as file:
    # for line in file:
        # We use split(",") to split the values
        # in the csv file by comma, returning the
        # elements as a list
        # We can assign them to multiple variables
        # to unpack them
        # name, home = line.rstrip().split(",")

        # We can store the name and home of the student
        # in a dictionary, and then append the dictionary
        # to a list so we can sort by name
        # student = {"name": name, "home": home}
        # students.append(student)
    # However, the split function will fail if any of the
    # values in the csv file also contains a comma, e.g.
    # an address
    # Instead, we will define a csv reader
    # This will read our file as a list of columns
    # reader = csv.reader(file)

    # Alternatively, we can use a dictionary reader
    # to read our file as a dictionary of columns
    # The first row of the file represents the keys
    reader = csv.DictReader(file)

    # We will iterate over each row of the reader and
    # append the values to our students list as dictionaires
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# Sort and display students
# We set the key so that the sorted() function
# will sort the list students by student name
# key accepts a function, but we do not have to define
# a new function just for this one use
# We can instead pass a lambda function
# We use the keyword lambda to pass a function with no name
# as an argument
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")