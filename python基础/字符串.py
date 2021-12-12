str1 = 'hello ' \
       'word'
print(type(str1))
print(str1)
str2 = "hello " \
       "word"
print(type(str2))
print(str2)
str3 = '''hello 
word'''
print(type(str3))
print(str3)
str4 = """hello 
word"""
print(type(str4))
print(str4)
str5 = "hello world"
print(str5[-1])
for value in str5:
    print(value)
str6 = "hello 'you' world"
print(str6)

name = "小明"
age = 18
height = 1.80
# 字符串格式化：任意版本均可的
str1 = "我叫%s，今年%s，身高%.1f" % (name, age, height)
print(str1)
# 字符串格式化：3.6版本后的f-string
str2 = f"我叫{name}，今年{age}，身高{height}"
print(str2)
# 字符串格式化:3.6版本前的fomat函数
str3 = "我叫{}，今年{}，身高{}".format(name, age, height)
print(str3)

str = "hello you world"
index = str.find("you")
print(index)
index = str.find("99")
print(index)
index = str.find("h", 0, 6)
print(index)
index = str.find("you", 0, 6)  # [0,6)包含开始索引，不包含结束索引
print(index)

str = "hello python2.5 python3.4 python3.6 python3.9"
new_str = str.replace("py", "Py")
print(new_str)
new_str = str.replace("py", "Py", 2)
print(new_str)

str = "hello world hello python"
new_str1 = str.split("\d")
print(str,type(str))
print(new_str1,type(new_str1))
str = "hello world hello python"
new_str2 = str.split(" ", maxsplit=1)  # 可指定最大分割次数
print(new_str2)
str = "hello world\thello\npython"
new_str3 = str.split()  # 默认以空白字符作为分割，包括：tab、空格、回车
print(new_str3)

str1 = "hello "
str2 = "world "
str3 = "python"
new_str = str1 + str2 + str3
print(new_str)

_str = "."
str_list = ["rose", "tom", "lily", "mike"]
new_str = _str.join(str_list)
print(new_str)
print()
_str = "0123456789"
print(_str)
print(_str[1])
print()
# 截取2~5位置的字符串
print(_str[1:5])
# 截取2~末尾的字符串
print(_str[1:])
# 截取开始~5位置的字符串
print(_str[:5])
# 每隔1个字符截取，字符串
print(_str[::2])
# 截取字符串末尾两个字符
print(_str[-2::])
# 字符串的逆序
print(_str[::-1])
student_dict = {"name": "rose", "age": "18", "height": "1.8"}
print(type(student_dict))
# 集合可以对列表去重，元素不会重复
my_set = {1, 2, 3, 1, 2, 3}
print(my_set)
print(type(my_set))

my_dict = {}
print(type(my_dict))
my_list = []
print(type(my_list))
my_tuple = ()
print(type(my_tuple))
# 注意：空集合不能只用大括号
my_set = set()
print(type(my_set))

my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(my_list)
my_set = set(my_list)
print(my_set)
my_list = list(my_set)
print(my_list)
print()
# 注意：列表转元组、集合
my_list = [1, 2, 3, 5, 3, 5]  # 注意：列表可以修改
my_tuple = (tuple(my_list))  # 注意：元组不能修改
print(my_tuple)
my_set = set(my_list)  # 注意：集合不能出现重复
print(my_set)
print(my_list)  # 注意：未赋值前，原列表内容不变
my_list = list(my_set)
print(my_list)
print()
# 字符串转换
my_str = "hello"
print(tuple(my_str))
print(set(my_str))
print()
my_list = list(my_str)
print(my_list)
my_str = my_set
print(my_str)
my_str = "".join(my_list)
print(my_str)

my_list = [1, 2, 3, 4, 5, 23, 4, ]
print(len(my_list))
my_set = set(my_list)
print(len(my_set))
# 切片：列表的逆序
print(my_list[::-1])

new_list = [5, 2, 67, 5]
print(my_list + new_list)
new_tuple = tuple(new_list)
my_tuple = tuple(my_list)
print(my_tuple + new_tuple)

print(my_list*2)
print("="*20+"华丽分割线"+"="*20)

