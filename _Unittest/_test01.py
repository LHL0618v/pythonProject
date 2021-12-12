import unittest

from tool import add


class Test01(unittest.TestCase):
    def test_01(self):
        data = add(1, 2)
        if data == 3:
            return True
        else:
            return False

    def test_02(self):
        data = add(20, 50)
        if data == 70:
            return True
        else:
            return False

    def test_03(self):
        data = add(10, 10)
        if data == 20:
            return True
        else:
            return False
