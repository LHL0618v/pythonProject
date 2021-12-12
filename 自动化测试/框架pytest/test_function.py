import pytest


# 函数名必须test开头，才能被pytest加载
@pytest.mark.skip(reason='无条件跳过')
@pytest.mark.a
def test_01():
    print(123)
    assert 1 == 1


@pytest.mark.b
def test_02():
    print("首个测试")
    assert 1 == 1


@pytest.mark.c
def test_03():
    print("首个测试")
    assert 1 == 2


@pytest.mark.skipif(1 == 1, reason='满足条件跳过')
@pytest.mark.smoke_case
def testWoNiuSale_01():
    print("首个测试")
    assert 1 == 1


def testWoNiuSale_02():
    print("首个测试")
    assert 1 == 2


class TestAdd(object):
    def test_04(self):
        assert 100 == 100


if __name__ == '__main__':
    # -s：将print语句的结果输出
    # __file__当前文件所在路径
    # pytest.main(['-s',__file__])
    # -v：以详细信息显示每条用例执行结果
    pytest.main(['-v', __file__])
    # -q：以极简的形式显示测试结果。
    # pytest.main(['-q', __file__])
"""
    -k 关键字：只匹配执行函数/类/方法包含该关键字的用例
    -x：遇到有fail的用例时，立即停止，常用于调试
    --maxfail=n：当失败的用例达到n条时，则停止测试
    -m：对用例进行标记，执行指定的用例 
"""

"""
命令行执行：
pytest 参数 脚本
py.test 参数 脚本
python -m pytest 参数 脚本
"""
