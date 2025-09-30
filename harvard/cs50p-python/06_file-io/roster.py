# This program will write data to a csv file

import csv

# Prompt the user for their name and home
name = input("What's your name? ")
home = input("What's your home? ")

# Open the roster.csv file in append mode
with open("roster.csv", "a") as file:
    # Use csv.writer to write data to the file as a list
    # writer = csv.writer(file)
    # writer.writerow([name, home])

    # Use csv.DictWriter to write data to the file as a dictionary
    # Provide fieldnames to tell which order the fields are in
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})