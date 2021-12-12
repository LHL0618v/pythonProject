import unittest
from parameterized import parameterized
# 必须导入该包，才能让unittest测试框架实现方法的参数化
from _Unittest.login import login

# 测试数据一般存放在JSON文件里
import json


# data通常通过读取JSON文件处理后获得
def build_data():
    data = []
    with open("data.json", "r", encoding="utf-8") as f:
        _list = json.load(f)
        for i in _list:
            # 列表中有几组数，就代表有几个用例
            data.append((i["username"], i["password"], i["expect"]))
    return data

print(build_data())
class TestLogin(unittest.TestCase):
    # 类级别的最先调用方法（所有方法最开始1次）
    @classmethod
    def setUpClass(cls) -> None:
        print("打开游览器")

    # 每个测试方法执行前都会先调用的方法
    def setUp(self) -> None:
        print("输入网址")

    # 使用参数化时，光标要放在参数化上方的代码块才能运行测试
    # 必须传递[(),()]或[[],[]]的这种格式作为变量给data
    # 且列表或元组内的值要按顺序与方法中的形参一一对应
    @parameterized.expand(build_data())
    def test_login(self, username, password, expect):
        # self.assertIn(预期结果，实际结果)断言用例预期结果是否包含于实际结果，包含返回Ture，不包含返回False
        # self.assertEqual(预期结果，实际结果)断言用例预期结果与实际结果是否相等，相等返回Ture，不等返回False
        self.assertEqual(expect, login(username, password))

    # 每个测试方法执行后都会最终调用的方法
    def tearDown(self) -> None:
        print("关闭页面")

    # 类级别的最终调用方法(所有方法结束后1次)
    @classmethod
    def tearDownClass(cls) -> None:
        print("关闭游览器")
