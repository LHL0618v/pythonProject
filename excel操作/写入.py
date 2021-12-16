import xlwings as xw
# 应用对象不是必须的，如果有,关闭文件后，必须关闭应用。
# app = xw.App(visible=False, add_book=False)
# wb = app.books.add()
wb = xw.Book()
sht = wb.sheets["sheet1"]
sht.range("a1").value = "范某某1"
# 写入一行
sht.range("a2:d2").value = [1, 2, 3, 4]
sht.range("a3").value = [5, 6, 7, 8]
# 写入一列
sht.range("a4").options(transpose=True).value = [5, 6, 7, 8]
# 写入行列
sht.range("a8").value = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
wb.save("C:/Users/LHL/Desktop/2.xlsx")
wb.close()
# 关闭应用对象
# app.quit()
