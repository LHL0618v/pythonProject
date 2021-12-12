class Item(object):
    def __init__(self, _name, _area):
        self.type = _name
        self.area = _area

    def __str__(self):
        return "%s 占地面积：%02f" % (self.type, self.area)


class House(object):
    def __init__(self, _name, _area):
        self.type = _name
        self.area = _area
        self.free_area = _area
        self.item_name = []

    def __str__(self):
        return "%s 总共面积：%0.2f 剩余面积：%0.2f 家具列表：%s" % (self.type, self.area, self.free_area, self.item_name)

    def add_item(self, item):
        if self.free_area >= item.area:
            self.item_name.append(item.type)
            self.free_area -= item.area
            print(self, f"{item}")
            print("添加成功")
        else:
            print(self, f"不足{item.type}的{item.area}\n添加失败")


h = House("豪宅", 100)
print(h)
TV = Item("超大电视", 40)
h.add_item(TV)
box = Item("大箱子", 50.1)
h.add_item(box)
