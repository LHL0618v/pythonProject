# 简单的函数：lambda 形参1,形参2.....:单行表达式或者单个函数调用
ret = (lambda a, b: a + b)(20, 30)
print(ret)
# 匿名函数可以起名，再调用
func = lambda a, b: a + b
ret = func(30, 30)
print(ret)


# 匿名函数可以当做参数，被其他函数调用
def foo(fn):
    ret = fn()
    print(ret)


foo(lambda: 10 - 2)
