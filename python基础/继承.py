class Father(object):
    def __init__(self):
        self.money = 999999

    def __str__(self):
        return "%d" % self.money

    def print_info(self):
        print("财产：%d" % self.money)


# 子类可以继承父类的属性和方法
class Son(Father):
    pass


son = Son()
print(son.money)
print(son)
son.print_info()


# 单继承：子类只继承一个父类
# 多层继承：多层传递方法和属性

class Animal(object):
    def eat(self):
        print("吃东西")


class Dog(Animal):
    def drink(self):
        print("喝东西")


class SupperDog(Dog):
    pass


dog1 = SupperDog()
dog1.drink()
dog1.eat()


class Animal(object):
    def __init__(self):
        self.type = "动物"

    def __str__(self):
        return "动物：%s" % self.type


# 子类可以对父类的方法进行重写
# 且通过子类创建的对象调用的方法只会执行重写后的同名方法
class Dog(Animal):
    def __init__(self):
        self.type = "可爱的小狗"

    def __str__(self):
        return "狗：%s" % self.type


class SupperDog(Dog):
    pass


dog2 = SupperDog()
print(dog2.type)
print(dog2)


# 多继承：一个子类继承多个父类

class SmallDog(object):
    def eat(self):
        print("吃很少")


class BigDog(object):
    def drink(self):
        print("大口喝水")


class MidDog(BigDog, SmallDog):
    pass


# 查看继承顺序 用__mro__方法打印出来
dog3 = MidDog()
dog3.eat()
dog3.drink()
print(MidDog.__mro__)


class SmallDog(object):
    def eat(self):
        print("吃很少")


class BigDog(object):
    def eat(self):
        print("吃很多")


# 当两个父类出现同名方法时，默认调用继承顺序里的最近上一个
class MidDog(BigDog, SmallDog):
    pass


dog4 = MidDog()
dog4.eat()


# 当你即想，在子类里重写方法又想保留父类同名方法时
class SmallDog(object):
    def eat(self):
        print("吃很少")


class BigDog(object):
    def eat(self):
        print("吃很多")


class MidDog(BigDog, SmallDog):
    def eat(self):
        print("吃中量")
        print("=" * 20)
        # 父类名.同名方法(self,形参1,...)
        # 指定调用哪个父类的同名方法
        SmallDog.eat(self)
        print("=" * 20)
        # 继承顺序中类名的下一个
        super(BigDog, self).eat()
        print("=" * 20)
        # 调用自己当前这个类的下一个
        super().eat()
        print("=" * 20)


dog5 = MidDog()
dog5.eat()
