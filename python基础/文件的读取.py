file = open("xxx.txt", "r")
ret = file.read(5)
# 读取 n 个字符
print(ret)
file.close()
# 读取多行，并返回列表
with open("xxx.txt", "r") as file:
    r_list = file.readlines()
    # 读取全部行
    for row in r_list:
        print(row, end="")

with open("xxx.txt", "r") as file:
    while True:
        data = file.readline()
        if not data:
            # data值为空：非假 -> 真
            break
        print(data, end="")
        print(type(data))
