import unittest
from _Unittest._testlogin import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
# 旧的运行方式：用的是unittest.TextTestRunner()生成运行对象
runner = unittest.TextTestRunner()
runner.run(suite)
