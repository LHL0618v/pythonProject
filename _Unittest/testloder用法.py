import unittest

# 实例化加载对象并添加用例，返回的是suite对象
# unittest.TestLoader().discover('用例所在的相对路径','用例的代码文件名')
# 用例的代码文件名可以使用*（任意多个字符）通配符
# suite = unittest.TestLoader().discover('.', "_test*.py")
# 使用默认加载对象并添加用例
suite = unittest.defaultTestLoader.discover("../_Unittest/", "_test*.py")
unittest.TextTestRunner().run(suite)
