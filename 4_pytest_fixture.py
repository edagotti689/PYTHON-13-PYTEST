# function   Run once per test
# class      Run once per class of tests
# module     Run once per module
# session    Run once per session

import pytest

@pytest.fixture()
def set_tear(request):
    print('\n Setup')
    yield
    print('\n Teardown')

def test_add(set_tear):
    print(' \n Add :')

def test_sub(set_tear):
    print('\n sub :')

'''
Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data. ... Pytest while the test is getting executed, will see the fixture name as input parameter

'''
