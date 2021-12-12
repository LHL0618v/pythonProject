user_list = [{"user_name": "lin", "user_password": "1"}]
while True:
    print("提示：1=注册，2=登陆，3=退出")
    try:
        active = int(input("请输入操作数："))
        # 一级界面的操作数
        if active == 1:
            print("进入注册页面......")
            register_name = input("请输入注册姓名：")
            register_password = input("请输入注册密码：")
            try:
                print("提示：1=确认注册，2=返回上一级")
                active1 = int(input("请输入二级操作数："))
                # 二级界面的操作数
                if active1 == 1:
                    if register_name == "" or register_password == "":
                        print("账号或密码不能为空")
                    else:
                        for user_info in user_list:
                            if user_info["user_name"] == register_name:
                                print("该账号已被注册")
                                print(user_list)
                                break
                        else:
                            register_info = {"user_name": register_name, "user_password": register_password}
                            user_list.append(register_info)
                            print("注册成功")
                            print(user_list)
                elif active1 == 2:
                    print("返回上一级")
                    continue
                else:
                    print("请不要乱来")
            except ValueError:
                print("请输入正确的二级操作数")
        elif active == 2:
            print("进入登陆页面......")
            login_name = input("请输入登录姓名：")
            login_password = input("请输入登录密码：")
            try:
                print("提示：1=确认登录，2=返回上一级")
                active2 = int(input("请输入二级操作数："))
                # 二级界面的操作数
                if active2 == 1:
                    if login_name == "" or login_password == "":
                        print("账号或密码不能为空")
                    else:
                        for user_info in user_list:
                            if user_info["user_name"] == login_name and user_info["user_password"] == login_password:
                                print("登录成功")
                                break
                        else:
                            print("账号或密码错误")
                elif active2 == 2:
                    print("返回上一级")
                    continue
                else:
                    print("请不要乱来")
            except ValueError:
                print("请输入正确的二级操作数")
        elif active == 3:
            print("退出所有页面.....")
            break
        else:
            print("请不要乱来")
    except ValueError:
        print("请输入正确操作数")
