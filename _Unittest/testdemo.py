import unittest

# version = 30

version = 29


class TestDemo(unittest.TestCase):
    # 无论任何条件直接跳过
    @unittest.skip("没有原因，就是不执行")
    def test_1(self):
        print("测试方法 1")

    def test_2(self):
        print("测试方法 2")

    # 满足条件后选择跳过
    @unittest.skipIf(version >= 30, "版本大于30，不用测试")
    def test_3(self):
        print("测试方法 3")
