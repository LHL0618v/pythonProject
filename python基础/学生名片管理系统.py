user_list = []


def menu():
    """学生菜单栏
    """
    print("=" * 30)
    print("=1.添加学生")
    print("=2.查询所有学生")
    print("=3.查询某个学生")
    print("=4.修改某个学生")
    print("=5.删除某个学生")
    print("=6.退出系统")
    print("=" * 30)


# 也可以用长字符串的方式输出
#     print("""
# ====================
# =1.添加学生
# =2.查询所有学生
# =3.查询某个学生
# =4.修改某个学生
# =5.删除某个学生
# =6.退出系统
# ====================
#     """)

def add_list(name):
    """
    添加学生
    :param name:
    :return:
    """
    for user_dict in user_list:
        if user_dict["name"] == name:
            print("学生已存在")
            break
    else:
        age = int(input("请输入年龄："))
        height = float(input("请输入身高："))
        city = str(input("请输入城市："))
        add_dict = {"name": name, "age": age, "height": height, "city": city}
        user_list.append(add_dict)
        print("添加成功")


def empty():
    print("暂无学生信息")


def not_found():
    print("该学生不存在")


def all_student():
    """
    查找全部学生
    :return:
    """
    print("序号\t姓名\t年龄\t身高\t城市")
    for n, user_dict in enumerate(user_list):
        print(f"{n + 1}\t{user_dict['name']}\t{user_dict['age']}\t{user_dict['height']}\t{user_dict['city']}")


def only_student():
    """
    查找单个学生
    :return:
    """
    name = input("请输入要查找的学生姓名：")
    print("序号\t姓名\t年龄\t身高\t城市")
    for n, user_dict in enumerate(user_list):
        if name == user_dict["name"]:
            print(f"{n + 1}\t{user_dict['name']}\t{user_dict['age']}\t{user_dict['height']}\t{user_dict['city']}")
            break
    else:
        not_found()


def replace_student():
    name = input("请输入要修改的学生姓名：")
    for n, user_dict in enumerate(user_list):
        if name == user_dict["name"]:
            print("旧信息： ")
            print("序号\t姓名\t年龄\t身高\t城市")
            print(f"{n + 1}\t{user_dict['name']}\t{user_dict['age']}\t{user_dict['height']}\t{user_dict['city']}")
            user_dict["name"] = str(input("请修改姓名："))
            user_dict["age"] = int(input("请修改年龄："))
            user_dict["height"] = float(input("请修改身高："))
            user_dict["city"] = str(input("请修改城市："))
            print("修改成功")
            break
    else:
        not_found()


def del_student():
    name = input("请输入要删除的学生姓名：")
    for n, user_dict in enumerate(user_list):
        if name == user_dict["name"]:
            print("删除信息： ")
            print("序号\t姓名\t年龄\t身高\t城市")
            print(f"{n + 1}\t{user_dict['name']}\t{user_dict['age']}\t{user_dict['height']}\t{user_dict['city']}")
            del user_list[n]
            print("删除成功")
            break
    else:
        not_found()


def main():
    while True:
        menu()
        try:
            i = int(input("请输入功能菜单的操作编号："))
            if i == 1:
                name = input("请输入姓名：")
                add_list(name)
            elif i == 2:
                if user_list:
                    all_student()
                else:
                    empty()
            elif i == 3:
                if user_list:
                    only_student()
                else:
                    empty()
            elif i == 4:
                if user_list:
                    replace_student()
                else:
                    empty()

            elif i == 5:
                if user_list:
                    del_student()
                else:
                    empty()

            elif i == 6:
                print("退出系统中...")
                break
            else:
                print("请输入1~6的数字")
        except ValueError:
            print("请输入数字......")


main()
