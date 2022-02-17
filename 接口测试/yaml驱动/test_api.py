import pytest


class TestApi:

    @pytest.mark.parametrize('args', ["百里", "星瑶", "依然"])
    def test_api01(self, args):
        print(args)

    @pytest.mark.parametrize('args,age', [["百里", 13], ["星瑶", 10]])
    def test_api02(self, args, age):
        print(args, age)

    @pytest.mark.parametrize('args', [["百里", 13], ["星瑶", 10], "依然"])
    def test_api03(self, args):
        print(args)


if __name__ == '__main__':
    pytest.main(['test_api.py'])
