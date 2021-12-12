a=123
print(a)
a=250
print(type(a))
b=True
print(type(b))
c=1.75
print(type(c))
d='你好'
print(type(d))
import keyword
print(keyword.kwlist)
student=1
age=18
name='小红'
height=1.60
print("我是学号%06d的%s，年龄为%d,身高为%.2f米"%(student,name,age,height))
password=input("请输入密码:")
print("你输入的密码是：%s"%password)
a=123
a_str=str(a)
print(type(a_str))
age=int(input("请输入你的年龄:"))
print("你的年龄是：%d"%age)
a=10**20
print(a)
holiday_name = input("请输入节日名称：")
if holiday_name == "冬至":
    print("回家团圆饭")
elif holiday_name == "中秋":
    print("参与博饼")
elif holiday_name == "春节":
    print("放爆竹")
else:
    print("在家睡觉")
while True:
    print("永不结束的死循环")
    input("")