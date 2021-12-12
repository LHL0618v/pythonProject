import time


# 装饰器的标准写法:传递函数，内函数返回最终结果，外函数返回内函数名
def get_run_time(func):  # 外函数
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)  # 调用被装饰的函数
        print(time.time() - start)  # 输出被装饰函数的运行时间
        return res

    return wrapper  # 外函数返回被装饰函数运行结果


@get_run_time
def fc(n):
    for i in range(n):
        print("*")
        time.sleep(0.2)


fc(5)


# 三层嵌套，可以为装饰器本身传参
def login(user, password):
    def outer(func):  # 外函数
        def inner(*args, **kwargs):
            if user == 'admin' and password == '123456':
                res = func(*args, **kwargs)  # 调用被装饰的函数
                return res  # 返回被装饰函数的运行结果
            else:
                print("登录失败 ")

        return inner  # 外函数返回被装饰函数运行结果

    return outer


name = "admin"


@login(name, "123456")
def add_customer(_name):
    print(f"新增{_name}成功")


add_customer(name)
