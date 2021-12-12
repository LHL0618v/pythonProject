import os

# # 批量修改文件名
# os.chdir("_test_")
# old_list = os.listdir()
# print(old_list)
# for old_name in old_list:
#     temp = "[海龙出品]-"
#     new_name = temp + old_name
#     os.rename(old_name, new_name)
# os.chdir("../")
# 批量恢复文件名
# os.chdir("__pytest")
# old_list = os.listdir()
# print(old_list)
# for old_name in old_list:
#     temp = "[海龙出品]-"
#     if old_name.find(temp) != -1:
#         new_name = old_name[len(temp):]
#         os.rename(old_name, new_name)
# os.chdir("../")


# 判断后再进行批量修改和恢复操作
os.chdir("../_test_")
old_list = os.listdir()
print(old_list)
for old_name in old_list:
    temp = "[海龙出品]-"
    # 如果有temp字符串，就进行恢复操作
    if old_name.find(temp) != -1:
        new_name = old_name[len(temp):]
        os.rename(old_name, new_name)
    # 如果没有temp字符串，就进行修改操作
    else:
        new_name = temp + old_name
        os.rename(old_name, new_name)
os.chdir("../../")