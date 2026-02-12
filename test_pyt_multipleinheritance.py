import pytest
class add:
    def add(self,a,b):
        return a+b
class sub:
    def sub(self,a,b):
        return a-b
class cal(add,sub):
    pass
def test_add():
    c = cal()
    if c.add(1,8) != 4:
        pytest.fail("Addition failed")

def test_sub():
    c = cal()
    result = c.sub(10, 5)
    if result != 5:
        pytest.fail("Subtraction test failed")

