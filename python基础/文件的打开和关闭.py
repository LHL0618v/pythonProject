#  "w" 打开文件，文件不存在创建，文件存在，清空内容
file = open("xxx.txt", "w")
file.close()
# 自动关闭文件
with open("xxx.txt", "w") as file:
    file.write("hello world\n")
    file.write("hello python\n")
    file.write("hello tom\n")

# 追加方式打开，不会清空内容，不能进行读操作
file = open("xxx.txt", "a")
file.write("hello kity")
file.close()
