# 函数的定义
def say_hello():
    """
    你好
    :return:
    """
    print("hello 1")
    print("hello 2")
    print("hello 3")


# 函数的调用
print("函数调用前")
say_hello()
print("函数调用后")


def num_sum(num1, num2):
    """
    两数求和
    :param num1: 任意整数
    :param num2: 任意整数
    :return:
    """
    sum = num1 + num2
    print(f"求和：{num1}+{num2}={sum}")


def num_subtraction(num1, num2):
    """
    两数求和
    :param num1: 任意整数
    :param num2: 任意整数
    :return:
    """
    subtraction = num1 - num2
    print(f"求减：{num1}-{num2}={subtraction}")


num1, num2 = map(int, input("请输入两个数字：").split())
num_sum(num1, num2)
num_subtraction(num1, num2)


def num_sum2(num1, num2):
    """
    两数求和
    :param num1: 任意整数
    :param num2: 任意整数
    :return:sum
    """
    result = num1 + num2
    return result


_sum = num_sum2(50, 20)
print(_sum)


# 函数默认返回值：None
def fool():
    print("^_^")


_res = fool()
print(_res)


# 函数默认返回值：None
def fool1():
    print("$_$")
    return


_res = fool1()
print(_res)


# return 会中断函数
def func():
    print("不努力，你来学代码干嘛")
    return
    print("我想玩游戏")


func()


# 无参无返回值的函数示例
def menu():
    """
    功能菜单
    :return:
    """
    print("=" * 20)
    print("=1.添加学生")
    print("=2.查询学生")
    print("=3.删除学生")
    print("=4.修改学生")
    print("=" * 20)


menu()


# 无参有返回值的函数示例
def get_pi():
    return 3.141592654


result = get_pi()
print(result)


# 有参无返回值的函数示例
def print_char(num, char):
    """
    打印指定数量的字符
    :return:
    """
    print(char * num)


print_char(2, "*")


# 有参有返回值的函数示例
def func_n(n):
    """
    实现1~n的累加
    :return:
    """
    i = 0
    sum = 0
    while i <= n:
        sum += i
        i += 1
    return sum


m = func_n(9)
print(f"1~9累加的结果:{m}")


# 函数的嵌套调用
def fun01():
    print("调用函数01开始")
    print("调用函数01结束")


def fun02():
    print("调用函数02开始")
    fun01()
    print("调用函数02结束")


fun02()


def function1(n, face):
    print(face * n)


def function2(m, n, face):
    i = 0
    while i < m:
        function1(n, face)
        i += 1


function2(2, 2, "^_^ ")


# 采用函数嵌套的方式求三个数的平均数
def function3(i, j, k):
    sum = i + j + k
    return sum


def function4(i, j, k):
    sum = function3(i, j, k)
    avg = sum / 3
    return avg


_res = function4(10, 20, 30)
print(f"三个数的平均值是{_res}")

# 函数内未声明时，访问的是局部变量，声明后可修改全局变量

num = 10


def func01():
    num = 250
    print(f"未声明时访问：{num}")


func01()
print(num)
print()


def func02():
    global num
    num = 250
    print(f"已声明时访问：{num}")


func02()
print(num)


#  关键字传参：形参=值
def foo(num1, num2, num3, num4):
    print(num1, num2, num3, num4)


#  且关键字参数必须在位置参数右侧
#  同一个形参不能重复传值
foo(1, 2, num4=4, num3=3)


# 默认参数：缺省形参必须在普通参数的右边
def foo01(a, b, c, d=40, e=50):
    print(a, b, c, d, e)


foo01(1, 2, 3, 4, 5)
foo01(1, 2, 3)
foo01(1, 2, 3, 4)


def foo03(a):
    print(a, type(a))


foo03(9)


# 不定长参数：先包装成元组，可以接收多个位置实参
def foo04(*args):
    print(args, type(args))


foo04(9, 9, 5, 2)


def foo05(name, age, sex):
    print(name, age, sex)


foo05(name="mike", age=18, sex="男")

# 字典型不定长参数：先包装成字典，可以接收多个关键字实参
# 字典型不定长参数：已经存在的形参对应的关键字实参不会包装到字典
# 字典型不定长参数：字典型的形参必须在形参列表最后边
def foo06(name, **kwargs):
    print(name, kwargs, type(kwargs))


foo06(name="mike", age=18, sex="男")
foo06(name="mike")
foo06("lily")


# 多种参数同时出现的函数定义模板
def foo07(name, *args, city="sz", **kwargs):
    print(name, args, city, kwargs)


# 1.关键字参数必须在位置参数右边
# 2.args：不定长的位置参数
# 3.kwargs:不定长的关键字参数

foo07("rose")
foo07("tom", city="bj")
foo07("rose", 18, "male")
foo07("rose", 18, "male", city="shenzhen", cls="python42期", like='python')
