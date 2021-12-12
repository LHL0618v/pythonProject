import unittest

# 实例化(创建对象)套件对象
# from _testcase01 import Test01
from _Unittest.study._testcase01 import Test01
from _Unittest.study._testcase02 import Test02
from _Unittest.study._testcase03 import Test03

suite = unittest.TestSuite()
# 使用套件对象添加用例方法一：套件对象.addTest(测试类名（'方法名')）
suite.addTest(Test01("test_method01"))
suite.addTest(Test01('test_method02'))
suite.addTest(Test02("test_method03"))
suite.addTest(Test02('test_method04'))
suite.addTest(Test03("test_method05"))
suite.addTest(Test03('test_method06'))
# 实例化运行对象
runner = unittest.TextTestRunner()
# 使用运行对象去执行套件对象
runner.run(suite)
