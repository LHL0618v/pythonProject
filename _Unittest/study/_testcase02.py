import unittest


# 自定义测试类，必须需要继承unittest.TestCas的类即可
class Test02(unittest.TestCase):
    # 测试方法必须以test_开头
    def test_method03(self):
        print("测试方法3")

    def test_method04(self):
        print("测试方法4")
# 光标放在类名后面运行，会执行类中所有方法
# 光标放在方法名后边运行，只执行当前方法

