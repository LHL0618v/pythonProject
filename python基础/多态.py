# 多态：调用同一个函数，不同表现
"""
1.实现继承关系
2.子类重写父类方法
3.通过对象调用该方法
"""

class Animal(object):
    def __str__(self):
        return "动物"


class Cat(Animal):
    def __str__(self):
        return "猫"


class Dog(Animal):
    def __str__(self):
        return "狗"


def fun(args):
    print(args)


dog = Dog()
fun(dog)

cat = Cat()
fun(cat)
