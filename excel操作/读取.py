import xlwings as xw
wb = xw.Book("C:/Users/LHL/Desktop/2.xlsx")
sht = wb.sheets["sheet1"]
# 读单元格
data = sht.range("a1").value
print(data)
# 读一行
data = sht.range("a2:d2").value
print(data,type(data))
# 读一列
data = sht.range("a4:a7").value
print(data)
# 读行列
data = sht.range("a8:c10").value
print(data)
wb.save()
wb.close()


