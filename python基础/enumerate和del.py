user_list = [{"name": "mike", "age": "34", "tel": "110"}, {"name": "yoyo", "age": "18", "tel": "120"}]
# 常规写法
i = 0
for r in user_list:
    print(i, r)
    i += 1
# enmuerarte 通过容器取索引的函数
for i, r in enumerate(user_list):
    print(i, r)
# del 删除对应下标的元素
print(user_list)
del user_list[0]
# 删除后会给元素重新分配下标
del(user_list[0])
print(user_list)
