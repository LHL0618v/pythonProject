import requests


def outer():  # 外函数
    age = 20  # 外函数变量

    def inner():  # 内函数
        print(age)  # 内函数引用外函数变量

    return inner  # 外函数返回内函数引用


f = outer()
print(type(f))
f()


# 使用闭包函数只需要传递一次url
def outer1(url):  # 外函数
    def inner1():  # 内函数
        r = requests.get(url)
        print(r.encoding)

    return inner1  # 外函数返回内函数引用


# 实际应用中，网络爬虫中比较实用
f1 = outer1("https://www.baidu.com/")
f1()
f1()


# 内函数中修改外函数的变量
def outer():  # 外函数
    age = 20  # 外函数变量

    def inner():  # 内函数
        nonlocal age # 声明变量不是本地变量（针对不可变的数据类型）
        age += 1
        print(age)  # 内函数引用外函数变量

    return inner  # 外函数返回内函数引用


f = outer()
print(type(f))
f()
