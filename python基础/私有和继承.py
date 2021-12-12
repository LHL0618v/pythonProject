class Animal(object):
    # 私有属性
    def __init__(self):
        self.__type = "动物"

    # 公有方法
    def print_info(self):
        print(self.__type)
        self.__leave()

    # 私有方法
    def __leave(self):
        print("休产假了")


# 子类无法直接访问父类的私有属性和私有方法
class Dog(Animal):
    pass


dog = Dog()
# 子类可以通过父类继承的公有方法访问父类私有属性和私有方法
dog.print_info()
