'''
1. Pytest is a testing framework which allows us to write test codes using python. 
'''
# To execute python file by pytest 
python -m pytest 1_pytest.py 
pytest 1_pytest.py 

# To get print function output on console
python -m pytest 1_pytest.py -s

# To Run particular testcase
python -m pytest 1_pytest.py -s -k test_add

# To Run particular testcases
python -m pytest 1_pytest.py -s -k test_

# To skip particular testcase
pytest 1_pytest.py -s -k " not test_a"





