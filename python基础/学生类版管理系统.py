# 处理过程中的对象列表
user_list = []


class Student(object):
    """
    学生类
    """

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return f"姓名：{self.name}\t年龄：{self.age}\t电话：{self.tel}"

    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'tel': self.tel}


class OperationNumError(Exception):
    """
    操作数异常
    """

    def __init__(self):
        super().__init__()
        self.len = 1
        self.type = "整数"

    def __str__(self):
        return "长度为%d的‘1~6’中的一位%s" % (self.len, self.type)


def load_info():
    """
    加载学生信息
    :return:
    """
    try:
        with open("学生名片.txt", "r") as file:
            data = file.read()
    except FileNotFoundError:
        print("文件不存在，无法加载学生信息")
    if data:
        te_user_list = eval(data)
        # 读写过程中的临时的字典列表：te_user_list
        for te_student in te_user_list:
            # te_user_list列表中的元素此时是字典，要转成对象才能处理
            student = Student(te_student['name'], te_student['age'], te_student['tel'])
            user_list.append(student)
    else:
        empty()


def save_info():
    """
    保存学生信息
    :return:
    """
    # 循环开始前要对字典列表进行清空，否则会重复添加
    te_user_list = []
    # 读写过程中的临时的字典列表：te_user_list
    for student in user_list:
        # 要将列表中的对象转成字典，才能写入到文件中，才能正常读取并识别。
        user_dict = student.to_dict()
        te_user_list.append(user_dict)
    try:
        with open("学生名片.txt", "w") as file:
            file.write(str(te_user_list))
    except FileNotFoundError:
        print("文件不存在,已重新生成")


def empty():
    print("暂无学生信息")


def noexist():
    print("查无此人")


def add():
    """
    添加学生
    :return:
    """
    add_name = input("姓名：")
    for student in user_list:
        if student.name == add_name:
            print("该学生已存在")
            break
    else:
        add_age = int(input("年龄："))
        add_tel = int(input("电话："))
        add_student = Student(add_name, add_age, add_tel)
        user_list.append(add_student)
        save_info()


def students():
    """
    打印全部学生信息
    :return:
    """
    if not user_list:
        empty()
        return
    for i, student in enumerate(user_list):
        print(i + 1, "\t", student)


def search():
    """
    查找某个学生
    """
    search_name = input("要查找的学生:")
    for i, student in enumerate(user_list):
        if student.name == search_name:
            print(i + 1, "\t", student)
            break
    else:
        noexist()


def change():
    """
    修改某个学生
    """
    change_name = input("要修改的学生:")
    for i, student in enumerate(user_list):
        if student.name == change_name:
            student.name = input("新的名字：")
            student.age = input("新的年龄：")
            student.tel = input("新的电话：")
            save_info()
            break
    else:
        noexist()


def del_stu():
    """
    删除某个学生
    """
    change_name = input("要删除的学生:")
    for i, student in enumerate(user_list):
        if student.name == change_name:
            del user_list[i]
            save_info()
            break
    else:
        noexist()


def main():
    load_info()
    while True:
        try:
            num = int(input("请输入操作数:"))
        except ValueError:
            print("请输入整数")
        else:
            if num == 1:
                add()
            elif num == 2:
                students()
            elif num == 3:
                search()
            elif num == 4:
                change()
            elif num == 5:
                del_stu()
            elif num == 6:
                print("退出系统")
                break
            else:
                print("请输入1~6")


main()
