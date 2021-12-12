class Dog(object):
    # 使用类创建对象时，会自动调用__init__方法
    # __init__方法给对象添加属性
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    # 打印对象时，自动调用的方法。返回值必须是字符串类型
    def __str__(self):
        return "我叫%s，今年%s岁" % (self.name, self.age)

    # 销毁对象：函数调用完毕，里面创建的对象，在对象生命周期结束时自动调用。
    def __del__(self):
        print("我悄悄的离开了..")

    def eat(self):
        print("%s 啃骨头" % self.name)

    def drink(self):
        print("%s 喝肉汤" % self.name)


# dog1 = Dog("旺柴", 18)
# print(dog1.name)
# dog1.eat()
# dog1.drink()
#
# dog2 = Dog("来福", 3)
# print(dog2.name)
# dog2.eat()
# dog2.drink()
# print(dog2)


def foo():
    dog3 = Dog("汤姆", 15)


print("调用函数前")
foo()
print("调用函数后")

dog4 = Dog("杰夫", 6)
del dog4  # del 对象：销毁对象，自动调用对象的__del__方法

dog5 = Dog("山福", 6)  # 程序结束，所有对象会被销毁。
