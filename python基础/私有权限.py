# 双下划线在属性或方法名字前，代表私有
class Dog(object):
    def __init__(self, _name):
        self.__body_count = 0
        self.name = _name

    def print_info(self):
        print(self.__body_count)
        self.__leave()

    # 私有方法也只能通过公有方法才能间接调用
    def __leave(self):
        print("休产假了")


dog1 = Dog("旺财")
print(dog1.name)
# 私有属性无法在类的外部使用对象直接访问
# print(dog1.__body_count )
# 私有属性可以通过公有方法间接访问
dog1.print_info()


