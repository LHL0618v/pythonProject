# __all__这个变量仅针对 from 模块名 import * 这个导入方式
__all__ = ["my_add"]


def my_add(a, b):
    """
    实现两个数相加
    :param a:第一个参数
    :param b:第二个参数
    :return:和
    """
    c = a + b
    return c


def my_sub(a, b):
    """
    实现两个数相减
    :param a: 第一个参数
    :param b: 第二个参数
    :return: 剩
    """
    c = a - b
    return c


#  直接运行模块文件，__name__的结果为__main__
# 此文件被当做模块导入时，，__name__的结果为模块名字符串
# 如果不想导入模块时，把模块内的测试代码运行，在测试代码放在if __name__ == "__main__":的条件语句里面
# if __name__ == "__main__":
# 输入main,会自动生成下一行代码
if __name__ == '__main__':
    ret = my_add(1, 3)
    print("测试求和的代码：", ret)

    ret = my_sub(3, 1)
    print("测试相减的代码：", ret)

    # 当直接在模块中执行__name__，为__main__
    # 当导入module时，__name__的值就变成了module(模块名)
    print("module中，__name__", __name__)
