# 创建一个整数列表：range(开始位置，结束位置，步长)，用法和字符串切片一样。
for i in range(0, 5):
    print(i)

for i in range(5):
    print(i)

sum = 0
for i in range(1,101):
    sum += i
print(sum)

# 开始位置和结束位置为对应值，非字符串切片里的下标
for i in range(5, 2,-1):
    print(i)

