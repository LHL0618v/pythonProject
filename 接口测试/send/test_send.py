import re
import requests
import pytest

from 接口测试.common.yaml_util import YamlUtil

"""
requests.get()
requests.post()
requests.put()
requests.delete()
requests.request()
响应：response对象
"""

"""
res = requests.request()
res.text:返回字符串数据
res.content:返回字节格式的数据
res.json():返回字典格式的数据
res.status_code:返回状态码
res.reason:返回状态信息
res.cookies:返回cookie信息
res.encoding:返回编码格式
res.headers:返回响应头
"""

"""
get请求通过params传递参数
post请求通过json或者data传参
    1、data
        数据报文：dict字典类型，那么默认情况下请求头：
       applilcattion/x-www-form-urlendcoded，表示以form表单的方式传参。格式：a=1&b=2&c=3
       数据报文：str类型，那么默认情况下：text/plain
    2、json
        数据报文：不管是dict还是str类型，请求头都是applilcattion/json,格式：{"a":1,"b":2}
"""


class TestSend(object):
    # 通过全局的类变量创建会话对象去封装接口自动化框架
    session = requests.session()

    @pytest.mark.smoke
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
        # 测试失败用例重跑设置的抛出异常
        # raise Exception("抛出一个异常")

    @pytest.mark.smoke
    def test_weixinpost(self):
        token = YamlUtil("extract.yml").read_yaml()["access_token"]
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=" + token
        data = {
            "tag": {"id": 134, "name": "广东人"}
        }
        # json.dumps():把字典格式的数据转换成str格式
        # json.loads()：把str格式的转换成字典格式
        res = requests.request("post", url=url, json=data)
        assert res.json()['errcode'] == 0

    @pytest.mark.smoke
    def test_filepost(self):
        token = YamlUtil("extract.yml").read_yaml()["access_token"]
        url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=" + token
        data = {
            # 文件上传必须以二进制的方式打开
            "media": open(r"H:/zhengjian.JPG", "rb")
        }
        res = requests.request("post", url=url, files=data)
        assert "url" in res.json()

    # 需要请求头的接口以及cookie关联的接口
    def test_shouyeget(self, coon_database):
        url = "http://47.107.116.139/phpwind/"
        res = TestSend.session.request("get", url=url)
        # 通过正则表达式获取鉴权码
        value = re.search('name="csrf_token" value="(.*?)"', res.text)[1]
        token = {"csrf_token": value}
        YamlUtil("extract.yml").write_yaml(token)
        assert "csrf_token" in res.text

    def test_loginpost(self):
        token = YamlUtil("extract.yml").read_yaml()["csrf_token"]
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            "username": "msxy",
            "password": "msxy",
            "csrf_token": token,
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        header = {
            "Accept": "application/json, text/javascript, /; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }
        res = TestSend.session.request("post", url=url, data=data, headers=header)
        assert res.json()['state'] == 'success'
