import unittest

# 实例化(创建对象)套件对象
# from _testcase01 import Test01
from _Unittest.study._testcase01 import Test01
from _Unittest.study._testcase02 import Test02
from _Unittest.study._testcase03 import Test03

suite = unittest.TestSuite()
# 使用套件对象添加用例方法二：将一个测试类中的所有方法进行添加
# 缺点：makeSuite 不会提示
suite.addTest(unittest.makeSuite(Test01))
suite.addTest(unittest.makeSuite(Test02))
suite.addTest(unittest.makeSuite(Test03))

# 实例化运行对象
runner = unittest.TextTestRunner()
# 使用运行对象去执行套件对象
runner.run(suite)

