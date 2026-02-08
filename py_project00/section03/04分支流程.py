"""
todo:Python里的switch匹配
    用到关键字match!
"""
from unittest import case

#
# day = int(input("请输入本日是周几"))
#
# match day:
#     case 1:
#         print("今天是周一")
#     case 2:
#         print("今天是周2")
#     case 3:
#         print("今天是周3")
#     case 4:
#         print("今天是周4")
#     case 5:
#         print("今天是周5")
#     case 6:
#         print("今天是周6")
#     case 0:
#         print("今天是周日")
#     case _:
#         print("输入有误！")

# 简易计算器

num01 = float(input("第一个数"))
oper = input("请输入要计算的运算符")
num02 = float(input("第2个数"))
# if oper == "+":
#     print(num01 + num02)
# elif oper == "-":
#     print(num01 - num02)
# elif oper == "*":
#     print(num01 * num02)
# elif oper == "/":
#     print(num01 / num02)
# else:
#     pass

match oper:
    case "+":
        print(f"{num01} + {num02} = {num01 + num02}")
    case "-":
        print(f"{num01} - {num02} = {num01 - num02}")
    case "*":
        print(f"{num01} * {num02} = {num01 * num02}")
    case "/" if num02 != 0:  # todo:如果if条件成立采取匹配,弱if不成立则跳转到case _:若没有则啥都不执行,也就是匹配不上而已
        print(f"{num01} / {num02} = {num01 / num02}")
    case _:
        print("不支持的算法")
