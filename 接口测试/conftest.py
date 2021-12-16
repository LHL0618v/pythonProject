import pytest

from 接口测试.common.yaml_util import YamlUtil


@pytest.fixture(scope="function", autouse=False)
def coon_database():
    print("连接数据库")
    # 类似teardown的功能，简单理解就是返回。
    # 和return区别在于，yield可以返回多次以及多个数据，且可以接代码。
    yield
    print("关闭数据库")


@pytest.fixture(scope="session", autouse=True)
# 默认前置函数：清空文件数据
def clear_yaml():
    YamlUtil('extract.yml').clear_yaml()
