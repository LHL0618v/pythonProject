import pytest
# 失败用例重跑三次，且只执行被标记为smoke的方法
# pytest.main(["--reruns=3","-m=smoke"])
pytest.main()
