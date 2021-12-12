class Dog(object):
    count = 0

    # 实例方法:需要创建实例对象，必须通过实例对象调用
    def print_count(self):
        self.count = 0
        print("实例", self.count)

    # 用装饰器标识其为类方法：调用类本身，可直接访问类属性
    @classmethod
    def print_count1(cls):
        print(cls.count)

    # 静态方法：不需要传类名也不需要传实例。
    # 有利于减少不必要的内存占用和性能消耗
    @staticmethod
    def print_count2():
        print("显示通用信息")


dog = Dog()
print(type(dog))
dog.print_count()
# 类方法推荐使用类名调用
Dog.print_count1()
# 静态方法推荐使用类名调用
Dog.print_count2()
