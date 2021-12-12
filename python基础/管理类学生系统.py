class Student(object):
    """
    学生类
    """

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return f"{self.name}\t\t{self.age}\t\t{self.tel}"

    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'tel': self.tel}


class Manage(object):
    def __init__(self):
        self.list = []

    def __str__(self):
        return "学生管理系统"

    @staticmethod
    def empty():
        print("暂无学生信息")

    @staticmethod
    def noexist():
        print("查无此人")

    @staticmethod
    def title():
        print("序号\t\t姓名\t\t年龄\t\t电话")

    @staticmethod
    def menu():
        """
        学生菜单栏
        """
        print("=" * 30)
        print("=1.添加学生")
        print("=2.查询所有学生")
        print("=3.查询某个学生")
        print("=4.修改某个学生")
        print("=5.删除某个学生")
        print("=6.退出系统")
        print("=" * 30)

    def load_info(self):
        """
        加载学生信息
        :return:
        """
        try:
            with open("学生名片.txt", "r") as file:
                data = file.read()
                if not data:
                    return self.empty()
                te_user_list = eval(data)
                # 读写过程中的临时的字典列表：te_user_list
                for te_student in te_user_list:
                    # te_user_list列表中的元素此时是字典，要转成对象才能处理
                    student = Student(te_student['name'], te_student['age'], te_student['tel'])
                    self.list.append(student)
                print("学生信息加载成功")
        except FileNotFoundError as e:
            print("文件不存在，无法加载", e)

    def save_info(self):
        """
        保存学生信息
        :return:
        """
        # 循环开始前要对字典列表进行清空，否则会重复添加
        te_user_list = []
        # 读写过程中的临时的字典列表：te_user_list
        for student in self.list:
            # 要将列表中的对象转成字典，才能写入到文件中，才能正常读取并识别。
            te_user_list.append(student.to_dict())
        try:
            with open("学生名片.txt", "w") as file:
                file.write(str(te_user_list))
        except FileNotFoundError:
            print("文件不存在,已重新生成")

    def students(self):
        """
        打印全部学生信息
        :return:
        """
        if not self.list:
            self.empty()
            return
        self.title()
        for i, student in enumerate(self.list):
            print(f"{i + 1}\t\t{student}")

    def add(self):
        add_name = str(input("姓名："))
        for student in self.list:
            if student.name == add_name:
                print("该学生已存在")
                break
        else:
            add_age = int(input("年龄："))
            add_tel = int(input("电话："))
            add_student = Student(add_name, add_age, add_tel)
            self.list.append(add_student)
            self.save_info()

    def search(self):
        """
        查找某个学生
        """
        search_name = input("要查找的学生:")
        self.title()
        for i, student in enumerate(self.list):
            if student.name == search_name:
                print(f"{i + 1}\t\t{student}")
                break
        else:
            self.noexist()

    def change(self):
        """
        修改某个学生
        """
        change_name = input("要修改的学生:")
        for student in self.list:
            if student.name == change_name:
                student.name = str(input("新的名字："))
                student.age = int(input("新的年龄："))
                student.tel = int(input("新的电话："))
                print("修改成功")
                self.save_info()
                break
        else:
            self.noexist()

    def del_stu(self):
        """
        删除某个学生
        """
        change_name = input("要删除的学生:")
        for i, student in enumerate(self.list):
            if student.name == change_name:
                del self.list[i]
                print("删除成功")
                self.save_info()
                break
        else:
            self.noexist()

    def start(self):
        self.load_info()
        self.menu()
        while True:
            try:
                num = int(input("请输入操作数:"))
            except ValueError:
                print("请输入整数")
            else:
                if num == 1:
                    self.add()
                elif num == 2:
                    self.students()
                elif num == 3:
                    self.search()
                elif num == 4:
                    self.change()
                elif num == 5:
                    self.del_stu()
                elif num == 6:
                    print("退出系统")
                    break
                else:
                    print("请输入1~6")


ms = Manage()
ms.start()
