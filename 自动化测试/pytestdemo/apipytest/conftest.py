import pytest


# 这里是第二个局部的夹具调用
@pytest.fixture(scope='function', params=['成龙', '甄子丹', '蔡依林'], ids=['parm01', 'parm02', 'parm03'], autouse=False,
                name='a')
def api_fixture(request):
    """
    scope:作用域——>>function（函数）/class（类）/module（模块）/package(包)/session(会话)
    params:参数化支持列表、元组、字典列表、字典元组。
            方法中必须设置形参request去接收params，且必须返回request.param才能实现参数传递。
    autouse:是否自动使用，默认为False(需要传递对应的函数名才能生效)
    ids:当使用params参数化时，给每个值设置一个变量名，意义不大。且不支持中文字符
    name:给表示被@pytest.fixture标记的方法取一个别名，当取了别名，原来的名称就用不了
    """
    print("\napi局部前置")
    # yield和return都表示返回，但return后面不能有代码,yield返回后面可以有代表
    yield request.param
    print("\napi局部后置")
    # return request.param
