import pytest


class Test(object):
    # 类中所有用例执行前后分别运行1次前置和后置
    def setup_class(self):
        print("\n类级前置")

    def teardown_class(self):
        print("\n类级后置")

    # _method可省略不写
    def setup_method(self):
        print("\n方法级前置")

    # 类中每条用例执行前后分别运行1次前置和后置
    def teardown_method(self):
        print("\n方法级后置")

    @pytest.mark.parametrize('a', [1, 2, 3, 4, 5])
    def test(self, a):
        print(a, end='')


if __name__ == "__main__":
    pytest.main(['-s', __file__])
