import unittest

# 使用第三方的运行对象并运行套件对象，并生成对应的html5文件
# HTMLTestRunner 网上下载的多数是py2的版本,语法结构不同会报错。
from HTMLTestRunner_PY3 import HTMLTestRunner

"""
实例化对象生成对应测试类的套件对象
from _Unittest._testlogin import TestLogin
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
"""
# 使用套件对象，加载对象去添加用例方法
suite = unittest.defaultTestLoader.discover('.', "_testlogin.py")
# 旧的运行方式：用的是unittest.TextTestRunner()生成运行对象
# runner = unittest.TextTestRunner()


# stream=sys.stdout 必填，测试报告的文件对象（open）,必须使用wb打开
# verbosity=1       可选，报告的详细程度，默认1-简略 2-详细
# descriptions=True 可选 可选，描述信息，python版本，pycharm版本
# title=None        可选，测试报告的标题
file = "report.html"
with open(file, "wb") as f:
    # 新的运行方式：通过第三方类生成第三方的运行对象
    runner = HTMLTestRunner(f, 2, "测试报告", "python3.9")
    # 运行对象执行套件时，要写在with缩进中
    runner.run(suite)

