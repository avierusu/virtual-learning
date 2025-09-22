# This program converts Astronomical Units (AU)
# into meters

def main():
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue
    
    print(f"{au} AU is {convert(au)} m")


# Convert AU to meters
def convert(au):
    # Check if the parameter au is an int or float
    if not isinstance(au, (int, float)):
        # If not, raise a type error
        raise TypeError("au must be an int or float")
    return au * 149597870700


if __name__ == "__main__":
    main()