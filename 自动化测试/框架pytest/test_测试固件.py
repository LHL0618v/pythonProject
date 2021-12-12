import pytest


@pytest.fixture(name='fx', scope='module',autouse=True)
def login():
    print("登录")


def test_add():
    print("添加会员")


def test_search(fx):
    print("库存查询")


if __name__ == "__main__":
    pytest.main(["-vs", __file__])
