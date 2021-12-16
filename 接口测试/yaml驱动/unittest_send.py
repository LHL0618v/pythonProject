import requests
import unittest
from ddt import ddt, file_data


@ddt
class Inter(unittest.TestCase):

    @file_data("config.yaml")
    def test_01_get_token(self, **kwargs):
        url = kwargs['request']['url']
        header = kwargs['request']['header']
        param = kwargs['request']['param']
        res = requests.request("get", url=url, headers=header, params=param)
        # 预期结果
        # expect = kwargs['request']['assert']['eq']['expires_in']
        # # 实际结果
        # actual = res.json()['expires_in']
        # # self.assertEqual(expect, actual)


"""
想办法处理多种结果的用例做断言
"""

if __name__ == "__main__":
    unittest.main()
