# import random as r
# 复杂的模块名简单化
# ret = r.randint(1, 3)
# print(ret)

from random import TWOPI as TP

TWOPI = 6.28

print(TWOPI)
print(TP)

# 模块搜索路径保存在sys.path变量
"""
1.在当前路径找
2.如果当前路径没有，就找系统路径
"""
import sys

print(sys.path)
