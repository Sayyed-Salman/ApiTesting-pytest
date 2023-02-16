"""
    Testing with pytest 
    pytest is a testing framework that makes it easy to write small tests,
    yet scales to support complex functional testing for applications and libraries.
"""

def test_addition():
    sum = 2 + 5 
    assert sum == 7

def test_subtraction():
    difference = 10 - 5
    assert difference == 5

def test_multiplication():
    product = 2 * 5
    assert product == 10

def test_uppercase():
    assert "hello".upper() == "HELLO"

