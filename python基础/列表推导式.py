_list = []
for i in range(5):
    _list.append(i)
print(_list)
# 计算公式 for 循环体 if判断
_list = [i for i in range(5)]
print(_list)

_list = [i * 2 for i in range(5)]
print(_list)

_list = [i for i in range(11) if i % 2 == 0]
print(_list) 
