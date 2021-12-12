import unittest

from _Unittest._test01 import Test01

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test01))
_run = unittest.TextTestRunner()
_run.run(suite)
