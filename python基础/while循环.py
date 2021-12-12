i = 0
k = 0
while i < 10:
    print("跑了第%d圈" % (i + 1))
    j = 0
    while j < 10:
        print("每圈做了%d个俯卧撑" % (j + 1))
        j += 1
    i += 1
    k += j
print("总共做了%d个俯卧撑" % k)

i = 1
m = 0
s = int(input("请输入需要累加最大数："))
while i <= s:
    m += i
    i += 1
print("累加的结果：%d" % m)

i = 1
m = 0
s = int(input("请输入需要累加最大数："))
while i <= s:
    if i % 2 == 0:
        m += i
    i += 1
print("累加所有偶数的结果：%d" % m)
