old_file_name = input("请输入要备份的文件名：\n")
pos = old_file_name.rfind(".")
new_file_name = old_file_name[:pos] + "[备份]" + old_file_name[pos:]
# 二级制的读写方式操作任意格式的文件，无需输入解码参数
f_r = open(old_file_name, "rb")
f_w = open(new_file_name, "wb")
while True:
    data = f_r.read(1024)
    f_w.write(data)
    if not data:
        # 如果data为空，就跳出循环
        break
f_r.close()
f_w.close()

