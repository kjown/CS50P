import pytest
from response import validate

def test_validate():
    assert validate("malan@harvard.edu") = True
    assert validate("own@yahoo.com") = True
    assert validate("malan@@@harvard.edu") = False
    assert validate("own@yahoo..com") = False
