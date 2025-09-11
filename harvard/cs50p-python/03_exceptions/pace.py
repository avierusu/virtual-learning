# This program demonstrates how to raise your own exception

def main():
    while True:
        try:
            miles = float(input("Enter miles to run: "))
        except ValueError:
            print("Invalid number of miles.")
        else:
            break
    
    while True:
        try:
            minutes = float(input("Enter minutes to run: "))
        except ValueError:
            print("Invalid number of minutes.")
        else:
            break
    
    pace = get_pace(miles, minutes)
    print(f"You need to run each mile in {round(pace, 2)} minutes")

def get_pace(mi, min):
    if not min > 0:
        raise ValueError("Minutes must be greater than 0.")
    
    return min / mi


main()