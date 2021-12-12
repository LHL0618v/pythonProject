import pytest
import requests

# 测试数据：每条用例的数据封包到一个元组
cases = [('输入正确信息登录成功', 'admin', '123456', '0000', 'login-pass'),
         ('用户名错误', 'admin1', '123456', '0000', 'login-fail'),
         ('密码错误', 'admin', '1234561', '0000', 'login-fail'),
         ('密码为空', 'admin', '', '0000', 'login-fail'),
         ('验证码错误', 'admin', '123456', '0001', 'vcode-error')]


# 测试函数声明了五个形参，用于接收用例对应的五个数据
@pytest.mark.parametrize('name, user, pwd, code, ex', cases)
def test_login(name, user, pwd, code, ex):
    print(name)
    # 建立会话对象
    rq = requests.session()
    url = 'http://47.92.203.151:8080/woniusales/user/login'
    login_data = {'username': user, 'password': pwd, 'verifycode': code}
    # 通过会话（可保持cookie等参数）发出请求
    r = rq.post(url=url, data=login_data)
    print(r.text)
    assert r.text == ex


# 测试函数声明了1个形参，用于接收一条元组代表的用例
@pytest.mark.parametrize('case', cases)
def test_login01(case):
    print(case[0])
    rq = requests.session()
    url = 'http://47.92.203.151:8080/woniusales/user/login'
    login_data = {'username': case[1], 'password': case[2], 'verifycode': case[3]}
    r = rq.post(url=url, data=login_data)
    assert r.text == case[4]


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
