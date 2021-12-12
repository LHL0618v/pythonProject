# 实例属性：
"""
1.通过__init__方法给实例对象添加的属性
2.在类的外面，。直接通过实例对象添加的属性
3.实例属性必须通过实例对象才能访问
"""
# 类属性：
"""
1.定义在类里面，类方法外卖的变量就是类属性
2.类属性可以使用类名或实例对象访问，推荐使用类名
"""


class Dog(object):
    # 类属性
    count = 0

    def __init__(self, _name):
        # 实例属性
        self.name = _name


print(Dog.count)
dog1 = Dog("大黄狗")
# 2.类属性可以使用类名或实例对象访问，推荐使用类名
print(dog1.count)
# 3.实例属性必须通过实例对象才能访问
print(dog1.name)

# 修改类属性
"""
类属性只能用类名修改，不能通过对象名修改
如果类属性名称与实例属性名称相同，实例对象名只能操作实例属性
"""
print("=" * 50)
Dog.count = 1
print("=" * 50)
# 实例对象.实例属性 =  值
dog1.count = 250  # 给dog1添加实例属性count = 250,不是修改类属性
print(dog1.count, Dog.count)


# 所有对象共有类属性
# 每个对象有自己的实例属性
class Dog(object):
    # 类属性
    count = 666

    def __init__(self):
        # 实例属性
        self.count = 888


dog1 = Dog()
print(dog1.count, Dog.count)


class Dog(object):
    # 私有类属性，无法在外面直接访问,可以通过公有方法，在类内部访问
    __count = 0

    def print_info(self):
        print(self.__count)


dog2 = Dog()
dog2.print_info()
