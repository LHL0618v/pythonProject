import pytest


# 函数名必须test开头，才能被pytest加载
@pytest.mark.a
class TestAdd(object):
    def test_03(self):
        assert 100 == 100


class TestWoNiuSale(object):
    def test_WoNiuSale(self):
        assert 120 == 100


if __name__ == '__main__':
    pytest.main(['-v', __file__])
"""
    -k 关键字：只匹配执行函数/类/方法包含该关键字的用例
    -x：遇到有fail的用例时，立即停止，常用于调试
    --maxfail=n：当失败的用例达到n条时，则停止测试
    -m：对用例进行标记，执行指定的用例
    .. 在项目根目录下新建 pytest.ini
    .. 在pytest.ini文件中添加标记
    .. 使用装饰器标记测试用例 @pytest.mark.标记
"""

"""
命令行执行：
pytest 参数 脚本
py.test 参数 脚本
python -m pytest 参数 脚本
"""
