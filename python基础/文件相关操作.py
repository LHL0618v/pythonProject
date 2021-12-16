import os

# 文件改名
# os.rename("xxx.txt", "xx.txt")
# 文件删除
# os.remove("xx.txt")
# 创建张三文件夹
# os.mkdir("张三")
# 获取运行脚本所在路径
path = (os.getcwd())
print(path)
# 切换到上一级路径并获取
# os.chdir("../")
# path = (os.getcwd())
# print(path)
# 获取当前路径下的所有文件信息：文件夹和文件的名字
dir_list = os.listdir()
print(dir_list)
# 判断文件是否存在
print(os.path.exists("x.txt"))
print(os.path.exists("xx.txt"))