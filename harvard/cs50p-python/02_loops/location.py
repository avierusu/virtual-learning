import sys

def main():
    # Create a Tuple to represent latitude and longitude
    coordinate_tuple = (42.376, -71.115)
    latitude, longitude = coordinate_tuple
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print()

    # Demonstrate the difference in memory allocation
    # between tuples and lists
    coordinate_list = [42.376, -71.115]
    print(f"Tuple: {sys.getsizeof(coordinate_tuple)} bytes")
    print(f"List: {sys.getsizeof(coordinate_list)} bytes")


main()