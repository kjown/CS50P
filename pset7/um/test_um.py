from um import count
import pytest

def test_count():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("yummy") == 0
    assert count("hello, um, python") == 1
    assert count("Um, thanks, um...") == 2
    assert count(" um ") == 1
    assert count("uM") == 1
    
