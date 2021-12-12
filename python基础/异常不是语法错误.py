#  可以捕获指定异常类型
try:
    # 未指定的异常无法捕获
    # if "18" > 18:
    #     print("年满18岁")
    print("=" * 30)
    print(10 / 0)
    print("=" * 30)
    f = open("xxx.txt", "r")
    print("=" * 30)
except (ZeroDivisionError, FileNotFoundError):
    print("捕获到被除数为0或找不到文件的异常")
# except :
#     print("不指定类型时，捕获任意异常")
# except ZeroDivisionError:
#     print("捕获到找不到文件的异常")
# except FileNotFoundError:
#     print("捕获到被除数为0的异常")


try:
    print("=" * 30)
    f = open("xxx.txt", "r")
    print("=" * 30)
except FileNotFoundError as s:
    print("异常信息描述：", s)

try:
    if "18" > 18:
        print("年满18岁")
    print("=" * 30)
    print(10 / 0)
    print("=" * 30)
    f = open("xxx.txt", "r")
    print("=" * 30)
except Exception as e:
    print("任意异常描述：", e)

try:
    f = open("xxx.txt", "r")
except Exception as e:
    print(type(e), "异常描述：", e)
else:
    print("没有发生异常")
finally:
    print("无论是否发生异常，都会执行的代码")

f = open("xxx.txt", "w")
try:
    # data = f.read()
    f.write("hello")
except Exception as e:
    print(type(e), "异常描述：", e)
else:
    print("文件操作成功")
finally:
    print("无论是否发生异常，都要关闭文件")
    f.close()
