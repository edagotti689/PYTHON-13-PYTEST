'''
1. Need to install pytest-xdist module to run test cases parallel.
    #  pip install pytest-xdist

2. To run test cases parallel we need to run like below
example : pytest -n 3 parllel_test_run.py -s

'''

import pytest
import time


def test_add():
    time.sleep(5)

def test_mul():
    time.sleep(5)

def test_sub():
    time.sleep(5)
