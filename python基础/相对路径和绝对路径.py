name = "a.txt"
# 绝对路径：路径的写法需要用反斜杠 /
f = open("F:/pythonProject/" + name, "w")
f.close()
# 相对路径  当前路径下的上一级写入方式打开或创建文件
name = "b.txt"
f = open("../" + name, "w")
f.close()
