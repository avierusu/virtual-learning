# This test file will be used to test the functionality
# of our square function we wrote
# We start our file with test_
from calculator import square
import pytest

# def test_square():
    # Check the functionality of the square function
    # If the actual value is not the expected
    # value, display an error message
    # if square(2) != 4:
    #     print("2 squared was not 4")
    # if square(3) != 9:
    #     print("3 squared was not 9")
    # We can use the keyword assert
    # If we assert a true statement, nothing will happen
    # If we assert a false statement, it will raise an
    # Assertion Error
    # assert square(2) == 4
    # assert square(3) == 9
    # assert square(-2) == 4
    # assert square(-3) == 9
    # assert square(0) == 0
    # We will use pytest to test this
    # we run the command pytest file_name.py

    # When pytest encounters an error and fails, all
    # further lines of code will not be executed and
    # tested
    # However, every function will be executed and
    # tested, so we can group our test cases
    # into separate functions

# We start our functions with test_ because that's
# what pytest will look for and run
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")