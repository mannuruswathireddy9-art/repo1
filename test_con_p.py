import pytest

class add:
    def __init__(self):
        print("Add class constructor called")

    def add(self, a, b):
        return a + b


class sub:
    def __init__(self):
        print("Sub class constructor called")

    def sub(self, a, b):
        return a - b


class cal(add, sub):
    def __init__(self):
        # Calling both parent constructors
        add.__init__(self)
        sub.__init__(self)
        print("Cal class constructor called")


def test_add():
    c = cal()
    if c.add(1, 5) != 4:
        pytest.fail("Addition failed")


def test_sub():
    c = cal()
    result = c.sub(10, 5)
    if result != 5:
        pytest.fail("Subtraction test failed")

