import pytest


@pytest.fixture(scope='function')
def all_fixture():
    """
    scope:作用域——>>function（函数）/class（类）/module（模块）/package(包)/session(会话)
    params:参数化支持列表、元组、字典列表、字典元组。
            方法中必须设置形参request去接收params，且必须返回request.param才能实现参数传递。
    autouse:是否自动使用，默认为False(需要传递对应的函数名才能生效)
    ids:当使用params参数化时，给每个值设置一个变量名，意义不大。且不支持中文字符
    name:给表示被@pytest.fixture标记的方法取一个别名，当取了别名，原来的名称就用不了
    """
    print("\n全局前置")
    yield
    print("\n全局后置")
