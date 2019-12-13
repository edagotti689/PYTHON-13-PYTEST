import pytest

## To run same test case repeatedly with different arguments
@pytest.mark.parametrize("a, b", [(1,11),(2,12), (3, 13),(4,14)])
def test_add(a, b):
    print(' \n SUM of {0} + {1} = {2}'.format(a,b, a + b))