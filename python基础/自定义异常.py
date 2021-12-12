# 自定义异常类
"""
1.必须继承于Exception
2.需重写__init__和__str__方法
3、__init__方法要调用父类的init，先初始化父类
"""


class NumError(Exception):
    def __init__(self, user_len, match_len=11):
        super().__init__()
        self.user_len = user_len
        self.match_len = match_len

    def __str__(self):
        return f"用户输入的电话位数为{self.user_len},要求输入长度为{self.match_len}"


try:
    num = input("请输入电话号码：")
    num_len = len(num)
    if num_len != 11:
        # 抛出异常类
        raise NumError(num_len)
except Exception as a:
    print(type(a), "异常描述", a)


