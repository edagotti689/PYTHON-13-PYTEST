import pytest

# It will run once before execute all test cases
def setup_module():
    print(' \n Suite Setup ')

# It will run once after execute all test cases
def teardown_module():
    print(' \n Suite Teardown')

def setup_function():
    print(' \n Setup Section ')

def teardown_function():
    print(' \n Teardown Section ')

def test_sub():
    print(' \n Test SUB')

def test_add():
    print(' \n Test ADD')
