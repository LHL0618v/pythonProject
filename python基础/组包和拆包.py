# 组包：将右侧多个值封装成元组
result = 1, 2, 3
print(result, type(result))
# 拆包：变量数量=容器长度，会一一对应容器的元素
a, b, c = result
print(a, b, c)
# 列表拆包
a, b, c = [10, 20, 30]
print(a, b, c)
# 字典拆包
a, b, c = {"key": "value1", "key2": "value2", "key3": "value3"}
print(a, b, c)
my_dict = {"key": "value1", "key2": "value2", "key3": "value3"}
for temp in my_dict.items():
    print(temp, type(temp))
    key, value = temp
    print(key, value)

for key, value in my_dict.items():
    print(key, value)
# 数据交换可以用组包丨拆包的方式
a = 100
b = 200
a, b = b, a
print(a, b)


# 函数返回多个数：拆包
def foo():
    return 1, 2, 3


ret = foo()
print(ret, type(ret))

r1, r2, r3 = foo()
print(r1, r2, r3)

# 引用的指向改变
a = 10
print(id(a), id(10))
b = a
print(id(a), id(b), id(10))
b = 20
print(id(a), id(b), id(20))
