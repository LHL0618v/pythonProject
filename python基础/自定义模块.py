from module import *

# 导入模块中“所有”功能，指__all__列举的功能

ret = my_add(1, 3)
print(ret)
# 不在__all__列表中的函数、类、变量等会报错
# ret = my_sub(3, 1)
# print(ret)

# 导入模块时，默认先执行模块中的内容
import module

ret = module.my_add(1, 3)
print(ret)

ret = module.my_sub(3, 1)
print(ret)
