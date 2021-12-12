# has_ticket = bool(input("是否有票："))
has_ticket = input("是否有票：")
print(type(has_ticket))
# if has_ticket == True:
if has_ticket == "是":
    print("正在进行安检")
    knife_length = int(input("刀具的长度："))
    if knife_length <= 20:
        print("允许上车")
    else:
        print("不许上车")
else:
    print("请先买票")