class SweetPotato(object):
    def __init__(self):
        self.state = "生的"
        self.time = 0
        self.condiment = "暂无"

    def __str__(self):
        return "地瓜%s,烧烤总时间:%d,佐料:%s" % (self.state, self.time, self.condiment)

    def cook(self, t1):
        self.time += t1
        if 0 <= self.time < 3:
            self.state = "生的"
        elif 3 <= self.time < 6:
            self.state = "半生不熟"
        elif 6 <= self.time <= 8:
            self.state = "熟了"
        elif self.time > 8:
            self.state = "烤糊了"
        return self.time, self.state

    def add_condiment(self, *args):
        if args:
            if self.condiment == "暂无":
                self.condiment = list(args)
            else:
                self.condiment = self.condiment.split(",")
                for data in list(args):
                    self.condiment.append(data)
            self.condiment = ",".join(self.condiment)


0
one = SweetPotato()
print(one)
one.cook(2)
one.add_condiment()
print(one)
one.cook(2)
one.add_condiment("酱油", "盐")
print(one)
one.cook(4)
one.add_condiment()
print(one)
one.cook(1)
one.add_condiment("米")
print(one)
