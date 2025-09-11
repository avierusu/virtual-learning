def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    # We can use this while loop to repeatedly
    # prompt until we don't get the value error
    while True:
        try:
            # If the user inputs any value that
            # cannot be casted to an integer,
            # a ValueError will be returned
            # We can use try to try the code,
            # and catch the ValueError with except
            # and do separate actions in that scenario
            return int(input(prompt))
            # We only want to try code that can produce
            # an error, so we don't want the print
            # statement here
        except ValueError:
            # print("x is not an integer")
            # We can use pass to continue without
            # taking action, but this doesn't
            # necessarily ignore the error; it is
            # still caught
            pass
        # else:
        #     # We can use else if there are no problems
        #     return x



main()