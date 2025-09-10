# String Slicing

def main():
    phone = "800-123-4567"
    # If we want to get only the area code (first 3 digits):
    # The first index is inclusive, and the second is exclusive
    # So we print the characters at indexes 0-2
    # We can leave the first or last blank
    print(phone[:3])
    # Or we can get the last 4 digits
    print(phone[-4:])


main()