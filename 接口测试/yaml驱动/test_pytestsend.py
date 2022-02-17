import requests
import pytest

from 接口测试.common.yaml_util import YamlUtil


class TestSend(object):
    # 通过全局的类变量创建会话对象去封装接口自动化框架
    session = requests.session()

    def test_weixinget(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type": "client_credential",
            "appid": "wx74a8627810cfa308",
            "secret": "e40a02f9d79a8097df497e6aaf93ab80"
        }
        res = requests.request("get", url=url, params=data)
        value = res.json()["access_token"]
        token = {"access_token": value}
        YamlUtil("extract.yml").write_yaml(token)
        assert "access_token" in res.json()


if __name__ == "__main__":
    pytest.main()
