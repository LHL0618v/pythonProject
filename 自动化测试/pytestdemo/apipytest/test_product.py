import pytest

version = "1.1.1"


class TestProduct:
    def test01(self, all_fixture, a):
        print("\n测试星瑶01")
        print("=" * 20)
        print(a)

    @pytest.mark.skipif(version == "1.1.1", reason="版本为1.1.1时跳过")
    def test02(self):
        print("测试星瑶02")
        assert 1 == 2

    @pytest.mark.usermanage
    def test03(self):
        print("测试星瑶03")

    @pytest.mark.smoke
    def test04(self):
        print("测试星瑶04")
