i = 0
m = "*"
while i < 5:
    j = 0
    while j < 5:
        print("%s " % m, end='')
        j += 1
    print()
    i += 1
i = 0
m = "*"
while i < 5:
    j = 0
    while j < i+1:
        print("%s " % m, end='')
        j += 1
    print()
    i += 1