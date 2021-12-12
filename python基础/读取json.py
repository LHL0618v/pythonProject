import json

# with open("info.json", "rb") as f:
with open("info.json", encoding="utf-8") as f:
    #  json.load 读取json的内容，最外层为{}即对象返回字典，最外层为[]即数值返回列表
    data = json.load(f)
    # get方法获取字典的值时，若key不存在，不会报错，返回的是默认值None
    print(data, type(data))
    for i, ret in enumerate(data):
        print(ret.get("name"), ret.get("age"), ret.get("sex"), ret.get("like")[2], ret.get("address").get("city"))


def read_data():
    with open("data.json", encoding="utf-8") as f:
        data = json.load(f)
        new_list = []
        for ret in data:
            _tuple = (ret.get('username'), ret.get('password'), ret.get('expect'))
            new_list.append(_tuple)
    return new_list

print(read_data())