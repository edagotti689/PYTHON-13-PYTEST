'''
mark - Mark nothing but a Tag name
     - We can run the test cases based on the requirement(unsequentialy)

pip install pytest-ordering
'''


import pytest


@pytest.mark.fourth
def first_sub(a,b):
    return a - b

@pytest.mark.third
def test_second():
    r = sub(10,5)
    assert r == 5 , ' \n Sub fun is not working as expected'
    print(' \n Test_sub Ran successfully')

@pytest.mark.first
def test_third():
    r = 5 + 5
    assert r == 10 , ' \n add is not working as expected'
    print(' \n Test_add Ran successfully')

@pytest.mark.second
def test_fourth():
    r = 5 * 5
    assert r == 25 , ' \n Mul is not working as expected'
    print(' \n Test_mul Ran successfully')


