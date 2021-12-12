name_list = ["jack", "mary", "sum", "KOOK", 1, 2, 3]
print(name_list[-2])
print(name_list[5])
school_list = [["北京大学", "清华大学"], ["中山大学", "华南理工大学"], ["哈工大", "哈工程"]]
print(school_list[0][1])
print(school_list[-1][0])
test_list = [5, 9, 10, 9, 1]
print(test_list)
test_list.append(100)
print(test_list)
test_list.remove(9)
print(test_list)
test_list[-1] = 0
print(test_list)
print(test_list[1])
print(len(test_list))
m = int(input("请输入任意数:"))
if m in test_list:
    print("在列表中")
else:
    print("不在列表中")
test_list.sort()
print(test_list)
test_list.sort(reverse=True)
print(test_list)
i = 0
while i < len(test_list):
    print(test_list[i], end=",")
    i += 1
print()
for num in test_list:
    print(num, end=",")
print()
name_list2 = ["ROSE", "TOM", "JACK", "MIKE"]
name = "ROSE"
if name in name_list2:
    print("%s在列表中" % name)
else:
    print("NO")
for name in name_list2:
    print(name, end=" ")
print()
name_tuple = ("ROSE", "TOM", "JACK", "MIKE")
name_list = ["ROSE", "TOM", "JACK", "MIKE"]
print(type(name_list))
print(type(name_tuple))
print(name_tuple[2])
name_tuple = (250)
print(type(name_tuple))
name_tuple = (250,)
print(type(name_tuple))
name_tuple = ("ROSE", "TOM", "JACK", "MIKE")
name = "JACK"
if name in name_tuple:
    print("%s在元组中" % name)
for name in name_tuple:
    print("%s" % name)
print(name_tuple[0])
print(len(name_tuple))
student_dict = {"name": "rose", "age": "18", "height": "1.8"}
print(student_dict)
print(student_dict["height"])
print(student_dict["name"])
student_dict["city"] = "shanghai"
print(student_dict)
student_dict["city"] = "hongkong"
print(student_dict)
height = student_dict.pop("height")
print(height)
print(student_dict)
print(student_dict["name"])
height = student_dict.get("height")
print(height)
height = student_dict.get("height", "默认值")
print(height)
# 遍历字典的key'键
for key in student_dict:
    print("%s" % key)
# 还需要显示值,但未赋值给任意变量
for key in student_dict:
    print("%s,%s" % (key, student_dict[key]))
# 通过方法遍历，并赋值给变量
for key, value in student_dict.items():
    print("%s,%s" % (key, value))
