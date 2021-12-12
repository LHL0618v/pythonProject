import pytest

# 模块中所有用例执行前后分别运行1次前置和后置
def setup_module():
    print("\n模块级前置")


def teardown_module():
    print("\n模块级后置")


# 模块中每条用例执行前后分别运行1次前置和后置
def setup_function():
    print("\n函数级前置")


def teardown_function():
    print("\n函数级后置")


@pytest.mark.parametrize('a', [1, 2, 3, 4, 5])
def test(a):
    print(a, end='')


if __name__ == "__main__":
    pytest.main(['-s', __file__])
