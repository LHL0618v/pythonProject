import unittest


# 自定义测试类，必须需要继承unittest.TestCas的类即可
class Test03(unittest.TestCase):
    # 测试方法必须以test_开头
    def test_method05(self):
        print("测试方法5")

    def test_method06(self):
        print("测试方法6")
# 光标放在类名后面运行，会执行类中所有方法
# 光标放在方法名后边运行，只执行当前方法

