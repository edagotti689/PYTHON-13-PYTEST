import pytest

def sub(a,b):
    return a - b

def test_sub():
    r = sub(10,5)
    assert r == 5 , ' \n Sub fun is not working as expected'
    print(' \n Test_sub Ran successfully')

def test_add():
    r = 5 + 5
    assert r == 10 , ' \n add is not working as expected'
    print(' \n Test_add Ran successfully')

def test_mul():
    r = 5 * 5
    assert r == 25 , ' \n Mul is not working as expected'
    print(' \n Test_mul Ran successfully')


