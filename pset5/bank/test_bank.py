import pytest
from bank import value

def test_return_0():
    assert value("hello bozo") == 0
    assert value("Hello") == 0


def test_return_20():
    assert value("hey") == 20
    assert value("hi") == 20

def test_return_100():
    assert value("What") == 100
    assert value("good morning") == 100


