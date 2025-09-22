from hello import say_hello

def test_default():
    assert say_hello() == "Hello, world"

def test_argument():
    assert say_hello("David") == "Hello, David"