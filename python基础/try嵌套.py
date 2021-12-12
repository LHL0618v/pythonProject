# try 异常在内部产生，但内部不捕获处理，会向外部传递
try:
    f = open("yyy", "w")
    try:
        ret = f.read()
        print(ret)
    finally:
        print("关闭文件")
        f.close()
except Exception as s:
    print(type(s), "外层捕获到的异常", s)


def test01():
    print("开始执行函数test011111")
    print(num)
    print("结束执行函数test011111")


def test02():
    print("开始执行函数test022222")
    test01()
    print("结束执行函数test022222")


def test03():
    print("开始执行函数test033333")
    try:
        test01()
    except Exception as e:
        print("外层函数捕获到异常：", e)
    print("结束执行函数test022222")


# test02()
test03()
