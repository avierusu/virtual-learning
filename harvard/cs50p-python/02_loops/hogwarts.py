# Print all students in a list
student_list = ["Hermione", "Harry", "Ron", "Draco"]

# For each loop:
for student in student_list:
    print(student)

# Alternatively, for loop:
print()
for index in range(len(student_list)):
    print(index + 1, student_list[index])


# Use a dictionary to assign houses to each student
# Pair a key (left) to a value (right)
students_dictionary = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# Print each student's house (value) using their name (key)
print()
for student in students_dictionary:
    print(student, students_dictionary[student], sep=", ")


# Use a list of dictionaries
# This lets us use names (keys) that we can understand
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

# Print out all the data
print()
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")