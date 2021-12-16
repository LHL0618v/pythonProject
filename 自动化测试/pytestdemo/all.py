import pytest
import os

# 命令行运行：pytest -vs test_login.py -n 2
"""
1、运行所有：pytest.main()
2、指定模块：pytest.main(['-vs', 'test_名.py'])
3、指定目录：pytest.main(['-vs', './目录名'])
4、通过nodeid指定用例运行：nodeid由模块名、分隔符、类名、方法名、函数名组成
 .. 书写格式如：pytest.main(['-vs', './apipytest/test_名.py::类名::test_函数名'])
"""
# pytest.main(['-vs', './apipytest/test_login.py', "-n=4"])
# pytest.main(['-vs', './apipytest/test_product.py', "--reruns=2"])
# pytest.main(['-vs', './apipytest/test_product.py'])
# pytest.main(['-vs', './apipytest/test_product.py'])
# pytest.main()
pytest.main()
os.system('allure generate ./apipytest/temp -o ./report --clean')
"""
-s：表示输出调试信息，包括print打印的信息
-v：显示更详细的信息
-vs:两个参数一起用
-n：支持多线程或者分布式运行测试用例
--reruns NUM：失败用例重跑NUM次（依赖插件pytest-rerunfailures，常用于UI自动化）
-x：表示有一个用例报错，那么测试停止
--maxfail=n：表示出现n个用例失败就停止
-k：根据测试用例的部分字符串指定测试用例 如：pytest -vs ./apipytest -k "ao"
"""

"""
unittest按ascll码的大小决定顺序
pytest默认至上而下执行顺序

通过装饰器可以改变默认的执行顺序
@pytest.mark.run(order=n)
n表示第几顺位
"""
