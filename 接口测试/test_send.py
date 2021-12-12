import requests
import pytest


class TestSend:
    token = ""

    def test_weixinget(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type": "client_credential",
            "appid": "wx6b11b3efd1cdc290",
            "secret": "106a9c6157c4db5f6029918738f9529d"
        }
        res = requests.get(url, data)
        TestSend.token = res.json().get("access_token")
        print(TestSend.token)

    def test_weixinpost(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=" + TestSend.token
        data = {
            "tag": {"id": 134, "name": "广东人"}
        }
        res = requests.post(url, json=data)
        print(res.json())

    def test_filepost(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=" + TestSend.token
        data = {
            "media": open("F:/zhengjian.JPG", "rb")
        }
        res = requests.post(url, files=data)
        print(res.json())


if __name__ == '__main__':
    pytest.main()
