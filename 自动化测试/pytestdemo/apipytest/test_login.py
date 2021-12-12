import pytest
import time


class TestLogin:
    # 所有用例之前只执行1次
    def setup_class(self):
        print("在每个类执行前的初始化的工作如：创建日志对象、创建数据库的连接、创建接口的请求对象")

    # 每个用例之前只执行1次
    def setup(self):
        print("\n测试用例之前执行的代码如：打开游览器，加载网页")

    @pytest.mark.skip(reason="无条件跳过")
    def test_01(self):
        time.sleep(1)
        print("测试百里01")

    @pytest.mark.run(order=2)
    def test_02(self):
        time.sleep(1)
        print("测试百里02")
        assert 1

    @pytest.mark.run(order=1)
    def test_03(self):
        time.sleep(1)
        print("测试百里03")

    @pytest.mark.smoke
    def test_04(self):
        time.sleep(1)
        print("测试百里04")

    def teardown(self):
        print("\n测试用例之后执行的代码如：关闭游览器，清除缓存")

    def teardown_class(self):
        print("在每个类执行后的扫尾工作如：销毁日志对象，销毁数据库连接，销毁接口的请求对象")
