a = 10 ** 20
print(a)
a = 9 / 5
print(a)
a = 9 // 5
print(a)
a = 9 % 5
print(a)
a = 9 * 5
print(a)
a = 9 - 5
print(a)
a = 9 + 5
print(a)
a = 2
c = 3
a += c
print(a)

age = int(input("请输入年龄："))
if age >= 18:
    print("允许进网吧嗨皮")
else:
    print("回家吃饭")

a = 10
b = 20
min_ = a if a < b else b
print(min_)

age = int(input("请输入年龄："))
print("允许进网吧嗨皮") if age >= 18 else print("回家吃饭")
