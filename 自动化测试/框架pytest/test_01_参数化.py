import pytest


@pytest.mark.parametrize('a,b,c', [(1, 2, 3), (3, 2, 1), (1, -1, 0)])
def test_01(a, b, c):
    assert a + b == c


if __name__ == '__main__':
    pytest.main('-v', __file__)
