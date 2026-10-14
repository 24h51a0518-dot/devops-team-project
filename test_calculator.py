from calculator import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

from calculator import multiply

def test_multiply():
    assert multiply(4, 3) == 12