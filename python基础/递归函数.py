# 递归函数：自己调用自己，一定要有出口（特定情况下，不再调用自身）
# 递归的最大深度为996次
def func(n):
    if n == 1:
        return 1
    else:
        ret = n * func(n - 1)
    return ret


ride = func(3)
print(f"阶乘：{ride}")
