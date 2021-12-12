# 定义一个类型
class Dog(object):
    # 定义方法是，self这个形参必须写。
    def eat(self):
        print("啃骨头", id(self))

    def drink(self):
        print("喝汤", id(self))


print(Dog)
dog1 = Dog()
dog1.eat()  # 调用对象方法时，self又解释器自动传递
dog1.drink()

"""
给对象添加属性：
1.创建对象变量
2.首次赋值时会定义属性，再次赋值改变属性。
"""
dog1.name = "旺柴"
dog1.age = 3
# self:调用方法时，就是对象本身
# self用于访问时，区分不同的对象和方法
print(dog1, id(dog1))
