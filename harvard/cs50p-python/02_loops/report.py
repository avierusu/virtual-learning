# Generate a report of a spaceship
def main():
    spacecraft1 = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft1))

    print()
    spacecraft2 = {"name": "James Webb Space Telescope"}
    # You can add a key and value after, like this:
    # spacecraft["distance"] = 0.01
    # or, to add multiple at once, use this:
    spacecraft2.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft2))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")}
    Orbit: {spacecraft.get("orbit", "Unknown")}


    ==========================
    """


main()