person_punches = input("请输入石头剪子布：")
if person_punches == "石头":
    person_punches = 1
elif person_punches == "剪子":
    person_punches = 2
elif person_punches == "布":
    person_punches = 3
else:
    print("请不要乱来")
import random
computer_punches = random.randint(1, 3)
if (person_punches == 1 and computer_punches == 2) or (person_punches == 2 and computer_punches == 3) or (
        person_punches == 3 and computer_punches == 1):
    print("恭喜你获胜")
elif person_punches == computer_punches:
    print("达成平局")
else:
    print("很遗憾，你失败了")
if computer_punches == 1:
    computer_punches = "石头"
elif computer_punches == 2:
    computer_punches = "剪子"
else:
    computer_punches = "布"
print("电脑出的拳是：%s" % computer_punches)
