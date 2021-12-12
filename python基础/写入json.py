import json
import webdriver
my_list = [('admin', '123456', '登录成功'), ('root', '123456', '登录失败'), ('admin', '123456', '登录失败')]

with open("new_info.json", "w", encoding="utf-8") as f:
    # json.dump(需要写入的’python中的数据类型‘，文件对象)
    json.dump(my_list, f, ensure_ascii=False, indent=2)
    # 直接显示中文，不以ASCII方式，indent代表缩进几位
